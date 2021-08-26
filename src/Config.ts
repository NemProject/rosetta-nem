import { BlockIdentifier, Currency, NetworkIdentifier, RosettaServer, Version } from 'rosetta-sdk-typescript';

export interface NetworkConfig {
    epochAdjustment: number;
    currencyMosaicId: string;
    restUrl: string;
    identifier: NetworkIdentifier;
    currency: Currency;
    version: Version;
    //Caching first block, rest endpoint is too slow. This can be moved to a better caching, indexer solution.
    genesisBlockIdentifier: BlockIdentifier;
}

export interface Config {
    networks: NetworkConfig[]; // it may support multiples networks.
}

export const testnet = (remote: boolean): Config => {
    const remoteRestUrl = 'http://hugetestalice2.nem.ninja:7890';
    return {
        networks: [
            {
                epochAdjustment: 1425859585, // in seconds
                currencyMosaicId: '091F837E059AE13C',
                restUrl: remote ? remoteRestUrl : 'http://localhost:7890',

                identifier: {
                    blockchain: 'Nem',
                    network: 'Testnet',
                },
                version: {
                    node_version: '1.0.1.0',
                    rosetta_version: RosettaServer.ROSETTA_API_VERSION,
                },
                currency: {
                    symbol: 'xem',
                    decimals: 6,
                },
                genesisBlockIdentifier: {
                    index: 1,
                    hash: 'f8c102ac15462c9f0e5629d0ea4f6fa0de80402763dbc48d946be2dda7c260ab',
                },
            },
        ],
    };
};

export const mainnet = (remote: boolean): Config => {
    const remoteRestUrl = 'http://hugealice2.nem.ninja:7890';
    return {
        networks: [
            {
                epochAdjustment: 1425859585, // in seconds
                currencyMosaicId: '091F837E059AE13C',
                restUrl: remote ? remoteRestUrl : 'http://localhost:7890/',
                identifier: {
                    blockchain: 'Nem',
                    network: 'Mainnet',
                },
                version: {
                    node_version: '1.0.1.0',
                    rosetta_version: RosettaServer.ROSETTA_API_VERSION,
                },
                currency: {
                    symbol: 'xem',
                    decimals: 6,
                },
                genesisBlockIdentifier: {
                    index: 1,
                    hash: '438cf6375dab5a0d32f9b7bf151d4539e00a590f7c022d5572c7d41815a24be4',
                },
            },
        ],
    };
};
