import {
    AccountApiService,
    AccountBalanceRequest,
    AccountBalanceResponse,
    AccountCoinsRequest,
    AccountCoinsResponse,
} from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';

export class AccountApiServiceImpl extends AbstractApiServer implements AccountApiService {
    async accountBalance(requestParameters: AccountBalanceRequest): Promise<AccountBalanceResponse> {
        return Promise.resolve(undefined);
    }

    async accountCoins(requestParameters: AccountCoinsRequest): Promise<AccountCoinsResponse> {
        return Promise.resolve(undefined);
    }
}
