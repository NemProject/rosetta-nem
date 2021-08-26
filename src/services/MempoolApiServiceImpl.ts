import {
    MempoolApiService,
    MempoolResponse,
    MempoolTransactionRequest,
    MempoolTransactionResponse,
    NetworkRequest,
} from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';
export class MempoolApiServiceImpl extends AbstractApiServer implements MempoolApiService {
    mempool(requestParameters: NetworkRequest): Promise<MempoolResponse> {
        return Promise.resolve(undefined);
    }

    mempoolTransaction(requestParameters: MempoolTransactionRequest): Promise<MempoolTransactionResponse> {
        return Promise.resolve(undefined);
    }
}
