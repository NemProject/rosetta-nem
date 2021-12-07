import { SearchApiService, SearchTransactionsRequest, SearchTransactionsResponse } from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';
export class SearchApiServiceImpl extends AbstractApiServer implements SearchApiService {
    searchTransactions(requestParameters: SearchTransactionsRequest): Promise<SearchTransactionsResponse> {
        return Promise.resolve(undefined);
    }
}
