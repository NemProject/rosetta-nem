import { expect } from 'chai';
import 'mocha';
import { ApiServiceFactoryImpl, testnet } from 'rosetta-nem';

const config = testnet(false);

const networkIdentifier = config.networks[0].identifier;

const serviceFactory = new ApiServiceFactoryImpl(config);

describe('Network Tests', () => {
    it('networkList', async () => {
        const networkClient = serviceFactory.network();
        const networkList = await networkClient.networkList();
        expect(networkList.network_identifiers).deep.eq(config.networks.map((n) => n.identifier));
    });

    it('networkOptions', async () => {
        const networkClient = serviceFactory.network();
        const networkOptions = await networkClient.networkOptions({
            network_identifier: networkIdentifier,
        });
        expect(networkOptions.version).deep.eq(config.networks[0].version);
    });
});
