import fetch from 'node-fetch';
import {
    BlockApi,
    BlockApiInterface,
    ChainApi,
    ChainApiInterface,
    Configuration,
    Middleware,
    ModelErrorDTOFromJSON,
    NodeApi,
    NodeApiInterface,
    RequestContext,
    ResponseContext,
} from 'rosetta-nem';

/**
 * Params used to create a nem client factory.
 */
interface NemRestClientFactoryParams {
    /**
     * The rest url of the NEM Rest service. E.g: http://hugetestalice2.nem.ninja:7890 , http://localhost:7890/
     */
    url: string;

    /**
     * Optional fetch api.
     */
    fetchApi?: unknown;

    /**
     * The optional client timeout in milliseconds.
     * TODO inject timeout to fetch.
     */
    timeout?: number;

    /**
     * Middleware for pre/post request customizations.
     */
    middleware?: Middleware[];
}

/**
 * When the rest client raises an error, the error will be wrapped in this exception.
 */
export class NemRestClientCallError extends Error {
    /**
     *
     * @param message - the message resolved from the error response
     * @param statusCode - the response status code
     * @param statusMessage - the response status message
     * @param body - the body as string
     */
    constructor(message: string, public readonly statusCode: number, public readonly statusMessage: string, public readonly body: string) {
        super(message);
    }
}

/**
 * Basic implementation of the exception handling middleware.
 */
export const exceptionHandlingMiddleware: Middleware = {
    async post(context: ResponseContext): Promise<Response | void> {
        const response = context.response;
        if (response.status >= 200 && response.status < 300) {
            return response;
        }
        throw await NemRestClientFactory.getErrorFromFetchResponse(response);
    },
};

/**
 * Main class used to create Rosetta rest clients.
 *
 * These rest client would most likely be used for Rosetta e2e testing as this sdk brings server side dependencies (e.g. express) you may not want in a Rosetta client.
 *
 */
export class NemRestClientFactory {
    private readonly configuration: Configuration;

    constructor(configs: NemRestClientFactoryParams) {
        const fetchApi = configs.fetchApi || (typeof window !== 'undefined' && window.fetch.bind(window)) || fetch;

        this.configuration = new Configuration({
            basePath: configs.url,
            fetchApi: fetchApi,
            middleware: configs.middleware || [
                exceptionHandlingMiddleware,
                {
                    pre(context: RequestContext): Promise<void> {
                        console.log(`Calling ${context.init.method} ${context.url} ${context.init.body || ''}`);
                        return Promise.resolve();
                    },
                },
            ],
        });
    }

    public static async getErrorFromFetchResponse(error: Response): Promise<NemRestClientCallError> {
        const statusCode = error?.status || 0;
        const statusMessage = (error?.statusText || 'Unknown Error').toString();
        const body = await error.text();

        const getMessage = () => {
            const defaultMessage = `${statusCode} - ${statusMessage}`;
            try {
                const modelError = ModelErrorDTOFromJSON(JSON.parse(body));
                return [modelError.error, modelError.status, modelError.message].join(' - ');
            } catch (e) {
                return defaultMessage;
            }
        };
        const message = getMessage();
        return new NemRestClientCallError(message, statusCode, statusMessage, body);
    }

    block(): BlockApiInterface {
        return new BlockApi(this.configuration);
    }
    chain(): ChainApiInterface {
        return new ChainApi(this.configuration);
    }

    node(): NodeApiInterface {
        return new NodeApi(this.configuration);
    }
}
