import { BlockApiService, BlockRequest, BlockResponse, BlockTransactionRequest, BlockTransactionResponse } from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';

export class BlockApiServiceImpl extends AbstractApiServer implements BlockApiService {
    async block(requestParameters: BlockRequest): Promise<BlockResponse> {
        return Promise.resolve(undefined);
    }

    blockTransaction(requestParameters: BlockTransactionRequest): Promise<BlockTransactionResponse> {
        return Promise.resolve(undefined);
    }
}
