import { EventsApiService, EventsBlocksRequest, EventsBlocksResponse } from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';
export class EventsApiServiceImpl extends AbstractApiServer implements EventsApiService {
    eventsBlocks(requestParameters: EventsBlocksRequest): Promise<EventsBlocksResponse> {
        return Promise.resolve(undefined);
    }
}
