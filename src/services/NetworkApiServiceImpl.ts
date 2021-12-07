import { Errors } from 'rosetta-nem';
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
        // REVISIT THIS POC IMPLEMENTATION!
        return {
            network_identifiers: this.config.networks.map((networkConfig) => networkConfig.identifier),
        };
    }

    async networkOptions(requestParameters: NetworkRequest): Promise<NetworkOptionsResponse> {
        // REVISIT THIS POC IMPLEMENTATION!
        const networkConfig = this.getConfiguration(requestParameters.network_identifier);
        return {
            allow: {
                balance_exemptions: [],
                call_methods: [],
                timestamp_start_index: networkConfig.epochAdjustment * 1000,
                historical_balance_lookup: true,
                mempool_coins: false,
                errors: Errors.getErrors(),
                operation_statuses: [],
                operation_types: [],
            },
            version: networkConfig.version,
        };
    }

    async networkStatus(requestParameters: NetworkRequest): Promise<NetworkStatusResponse> {
        return Promise.resolve(undefined);
    }
}
