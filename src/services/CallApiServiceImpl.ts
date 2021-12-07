import { CallApiService, CallRequest, CallResponse } from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';
export class CallApiServiceImpl extends AbstractApiServer implements CallApiService {
    call(requestParameters: CallRequest): Promise<CallResponse> {
        return Promise.resolve(undefined);
    }
}
