import { Config, Errors, NetworkConfig } from 'rosetta-nem';
import { NetworkIdentifier, ServerError } from 'rosetta-sdk-typescript';

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
}
