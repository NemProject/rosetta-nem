import { Express } from 'express';
import { ApiServiceFactoryImpl, mainnet, testnet } from 'rosetta-nem';
import { RosettaServer } from 'rosetta-sdk-typescript';

const args = process.argv;
const useRemoteUrl = !!args.find((arg) => arg.toLowerCase() == '--remote');
const useTestnet = !!args.find((arg) => arg.toLowerCase() == '--testnet');

const apiServiceFactory = new ApiServiceFactoryImpl(useTestnet ? testnet(useRemoteUrl) : mainnet(useRemoteUrl));

const logger = (app: Express) => {
    app.use((req, res, next) => {
        console.log(`Processing ${req.method} ${req.originalUrl}`);
        next();
    });
};

new RosettaServer({ apiServiceFactory, appSetupCallback: logger }).start(8080).catch((e) => {
    console.error(e);
});
