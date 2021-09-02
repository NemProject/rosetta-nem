import {
    ConstructionApiService,
    ConstructionCombineRequest,
    ConstructionCombineResponse,
    ConstructionDeriveRequest,
    ConstructionDeriveResponse,
    ConstructionHashRequest,
    ConstructionMetadataRequest,
    ConstructionMetadataResponse,
    ConstructionParseRequest,
    ConstructionParseResponse,
    ConstructionPayloadsRequest,
    ConstructionPayloadsResponse,
    ConstructionPreprocessRequest,
    ConstructionPreprocessResponse,
    ConstructionSubmitRequest,
    TransactionIdentifierResponse,
} from 'rosetta-sdk-typescript';
import { AbstractApiServer } from './AbstractApiServer';

export class ConstructionApiServiceImpl extends AbstractApiServer implements ConstructionApiService {
    constructionDerive(requestParameters: ConstructionDeriveRequest): Promise<ConstructionDeriveResponse> {
        return Promise.resolve(undefined);
    }

    constructionHash(requestParameters: ConstructionHashRequest): Promise<TransactionIdentifierResponse> {
        return Promise.resolve(undefined);
    }

    constructionMetadata(requestParameters: ConstructionMetadataRequest): Promise<ConstructionMetadataResponse> {
        return Promise.resolve(undefined);
    }

    constructionCombine(requestParameters: ConstructionCombineRequest): Promise<ConstructionCombineResponse> {
        return Promise.resolve(undefined);
    }

    constructionParse(requestParameters: ConstructionParseRequest): Promise<ConstructionParseResponse> {
        return Promise.resolve(undefined);
    }

    constructionPayloads(requestParameters: ConstructionPayloadsRequest): Promise<ConstructionPayloadsResponse> {
        return Promise.resolve(undefined);
    }

    constructionPreprocess(requestParameters: ConstructionPreprocessRequest): Promise<ConstructionPreprocessResponse> {
        return Promise.resolve(undefined);
    }

    async constructionSubmit(requestParameters: ConstructionSubmitRequest): Promise<TransactionIdentifierResponse> {
        return Promise.resolve(undefined);
    }
}
