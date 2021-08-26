import {
    BlockApiService,
    BlockRequest,
    BlockResponse,
    BlockTransactionRequest,
    BlockTransactionResponse,
    ServerError,
} from 'rosetta-sdk-typescript';
import { Errors } from '../Errors';
import { Operations, TransactionType } from '../Operations';
import { AbstractApiServer } from './AbstractApiServer';

export class BlockApiServiceImpl extends AbstractApiServer implements BlockApiService {
    async block(requestParameters: BlockRequest): Promise<BlockResponse> {
        const networkConfig = this.getConfiguration(requestParameters.network_identifier);
        const restClientFactory = this.getNemRestClientFactory(requestParameters.network_identifier);

        if (requestParameters.block_identifier.hash) {
            throw ServerError.rosettaError({
                ...Errors.BLOCK_BY_HASH_IS_NOT_SUPPORTED,
                description: `NEM does not support block by hash (YET)`,
            });
        }

        if (!requestParameters.block_identifier.index) {
            throw ServerError.rosettaError(Errors.BLOCK_HEIGHT_IS_REQUIRED);
        }

        const blockClient = restClientFactory.block();
        const block = await blockClient.blockAtPublic({
            blockAtPublicRequestDTO: {
                height: requestParameters.block_identifier.index,
            },
        });

        const blockIdentifier = await this.getBlockIdentifier(blockClient, block.height);
        const parentBlockIdentifier =
            block.height == 1
                ? blockIdentifier
                : {
                      index: block.height - 1,
                      hash: block.prevBlockHash.data,
                  };
        return {
            block: {
                parent_block_identifier: parentBlockIdentifier,
                block_identifier: blockIdentifier,
                transactions: block.transactions.map((transaction) => ({
                    operations: [
                        {
                            // COMPLETE EVERYTHING!
                            type: Operations.toOperation(transaction.type as TransactionType),
                            operation_identifier: {
                                index: 0,
                            },
                        },
                    ], // COMPLETE OPERATIONS! How to map operations to transactions?
                    transaction_identifier: {
                        hash: transaction.signature, // THIS OF COURSE NOT THE HASH, need to serialize and get the hash as the endpoint doesn't return it.
                    },
                })),
                timestamp: (block.timeStamp + networkConfig.epochAdjustment) * 1000,
            },
        };
    }

    blockTransaction(requestParameters: BlockTransactionRequest): Promise<BlockTransactionResponse> {
        return Promise.resolve(undefined);
    }
}
