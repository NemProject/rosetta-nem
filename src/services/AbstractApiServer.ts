import { BlockApiInterface, Config, Errors, NemRestClientFactory, NetworkConfig } from 'rosetta-nem';
import { BlockIdentifier, NetworkIdentifier, ServerError } from 'rosetta-sdk-typescript';

export abstract class AbstractApiServer {
    constructor(protected readonly config: Config) {}

    public getConfiguration(identifier: NetworkIdentifier): NetworkConfig {
        const config = this.config.networks.find(
            (networkConfig) =>
                networkConfig.identifier.network === identifier.network && networkConfig.identifier.blockchain === identifier.blockchain,
        );
        if (!config) {
            throw ServerError.rosettaError({
                ...Errors.NETWORK_IDENTIFIER_IS_INVALID,
                description: `There is no config with identifier ${identifier.blockchain} - ${identifier.network}`,
            });
        }
        return config;
    }

    public getNemRestClientFactory(identifier: NetworkIdentifier): NemRestClientFactory {
        const config = this.getConfiguration(identifier);
        return new NemRestClientFactory({
            url: config.restUrl,
        });
    }

    protected async getBlockIdentifier(blockClient: BlockApiInterface, height: number): Promise<BlockIdentifier> {
        const block = await blockClient.blockAtPublic({
            blockAtPublicRequestDTO: {
                height: height + 1,
            },
        });
        return {
            index: height,
            hash: block.prevBlockHash.data,
        };
    }
}
