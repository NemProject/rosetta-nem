import { Errors, Operations, OperationStatusObjects } from 'rosetta-nem';
import {
    NetworkApiService,
    NetworkListResponse,
    NetworkOptionsResponse,
    NetworkRequest,
    NetworkStatusResponse,
} from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';

export class NetworkApiServiceImpl extends AbstractApiServer implements NetworkApiService {
    async networkList(): Promise<NetworkListResponse> {
        return {
            network_identifiers: this.config.networks.map((networkConfig) => networkConfig.identifier),
        };
    }

    networkOptions(requestParameters: NetworkRequest): Promise<NetworkOptionsResponse> {
        const networkConfig = this.getConfiguration(requestParameters.network_identifier);
        return Promise.resolve({
            allow: {
                balance_exemptions: [],
                call_methods: [],
                timestamp_start_index: networkConfig.epochAdjustment * 1000,
                historical_balance_lookup: true,
                mempool_coins: false,
                errors: Errors.getErrors(),
                operation_statuses: OperationStatusObjects.getStatusList(),
                operation_types: Operations.getOperations(),
            },
            version: networkConfig.version,
        });
    }

    async networkStatus(requestParameters: NetworkRequest): Promise<NetworkStatusResponse> {
        const networkConfig = this.getConfiguration(requestParameters.network_identifier);
        const restClientFactory = this.getNemRestClientFactory(requestParameters.network_identifier);

        const chainClient = restClientFactory.chain();
        const nodeClient = restClientFactory.node();

        const peers = await nodeClient.nodePeerListReachable();
        const currentBlock = await chainClient.chainLastBlock();
        return {
            genesis_block_identifier: networkConfig.genesisBlockIdentifier,
            current_block_identifier: await this.getBlockIdentifier(restClientFactory.block(), currentBlock.height - 1),
            oldest_block_identifier: networkConfig.genesisBlockIdentifier,
            peers: peers.data.map((peer) => ({
                peer_id: peer.identity.name,
            })),
            current_block_timestamp: (currentBlock.timeStamp + networkConfig.epochAdjustment) * 1000,
        };
    }
}
