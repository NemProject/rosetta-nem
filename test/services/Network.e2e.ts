import 'mocha';
import { ApiServiceFactoryImpl, testnet } from 'rosetta-nem';
import { RosettaRestClientFactory, RosettaServer } from 'rosetta-sdk-typescript';

const config = testnet(true);
const apiServiceFactory = new ApiServiceFactoryImpl(config);
const server = new RosettaServer({ apiServiceFactory });
const port = 9000;
const serverUrl = `http://localhost:${port}`;
const restClientFactory = new RosettaRestClientFactory({
    url: serverUrl,
});

const networkIdentifier = config.networks[0].identifier;

describe('Network Tests', () => {
    before(() => {
        return server.start(port);
    });

    after(() => {
        return server.stop();
    });
    it('networkList', async () => {
        const networkClient = restClientFactory.network();
        const networkList = await networkClient.networkList({
            metadataRequest: {
                metadata: {
                    someMeta: 'request',
                },
            },
        });
        console.log(JSON.stringify(networkList, null, 2));
    });

    it('networkOptions', async () => {
        const networkClient = restClientFactory.network();
        const networkOptions = await networkClient.networkOptions({
            networkRequest: {
                network_identifier: networkIdentifier,
            },
        });
        console.log(JSON.stringify(networkOptions, null, 2));
    });

    it('networkStatus', async () => {
        const networkClient = restClientFactory.network();
        const networkStatus = await networkClient.networkStatus({
            networkRequest: {
                network_identifier: networkIdentifier,
            },
        });
        console.log(JSON.stringify(networkStatus, null, 2));
    });
});
