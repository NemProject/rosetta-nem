import {
    AccountApiServiceImpl,
    BlockApiServiceImpl,
    CallApiServiceImpl,
    Config,
    ConstructionApiServiceImpl,
    EventsApiServiceImpl,
    MempoolApiServiceImpl,
    NetworkApiServiceImpl,
    SearchApiServiceImpl,
} from 'rosetta-nem';
import { AccountApiService, ApiServiceFactory } from 'rosetta-sdk-typescript';

/**
 *
 */
export class ApiServiceFactoryImpl implements ApiServiceFactory {
    constructor(private readonly config: Config) {}

    account(): AccountApiService {
        return new AccountApiServiceImpl(this.config);
    }

    block(): BlockApiServiceImpl {
        return new BlockApiServiceImpl(this.config);
    }

    call(): CallApiServiceImpl {
        return new CallApiServiceImpl(this.config);
    }

    construction(): ConstructionApiServiceImpl {
        return new ConstructionApiServiceImpl(this.config);
    }

    events(): EventsApiServiceImpl {
        return new EventsApiServiceImpl(this.config);
    }

    mempool(): MempoolApiServiceImpl {
        return new MempoolApiServiceImpl(this.config);
    }

    network(): NetworkApiServiceImpl {
        return new NetworkApiServiceImpl(this.config);
    }

    search(): SearchApiServiceImpl {
        return new SearchApiServiceImpl(this.config);
    }
}
