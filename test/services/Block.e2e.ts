import 'mocha';
import { ApiServiceFactoryImpl, testnet } from 'rosetta-nem';
import { RosettaRestClientFactory, RosettaServer } from 'rosetta-sdk-typescript';
const config = testnet(true);
const apiServiceFactory = new ApiServiceFactoryImpl(config);
const server = new RosettaServer({ apiServiceFactory: apiServiceFactory });
const port = 9000;
const serverUrl = `http://localhost:${port}`;
const restClientFactory = new RosettaRestClientFactory({
    url: serverUrl,
});
const networkIdentifier = config.networks[0].identifier;
describe('Block Tests', () => {
    before(() => {
        return server.start(port);
    });

    after(() => {
        return server.stop();
    });
    it('block', async () => {
        const blockClient = restClientFactory.block();
        const block = await blockClient.block({
            blockRequest: {
                network_identifier: networkIdentifier,
                block_identifier: {
                    index: 100,
                },
            },
        });
        console.log(JSON.stringify(block, null, 2));
    });
});
