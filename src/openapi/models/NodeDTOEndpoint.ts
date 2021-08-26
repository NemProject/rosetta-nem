/* tslint:disable */
/**
 *
 * @export
 * @interface NodeDTOEndpoint
 */
export interface NodeDTOEndpoint {
    /**
     *
     * @type {string}
     * @memberof NodeDTOEndpoint
     */
    protocol: string;
    /**
     *
     * @type {number}
     * @memberof NodeDTOEndpoint
     */
    port: number;
    /**
     *
     * @type {string}
     * @memberof NodeDTOEndpoint
     */
    host: string;
}

export function NodeDTOEndpointFromJSON(json: any): NodeDTOEndpoint {
    return NodeDTOEndpointFromJSONTyped(json, false);
}

export function NodeDTOEndpointFromJSONTyped(json: any, ignoreDiscriminator: boolean): NodeDTOEndpoint {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        protocol: json['protocol'],
        port: json['port'],
        host: json['host'],
    };
}

export function NodeDTOEndpointToJSON(value?: NodeDTOEndpoint | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        protocol: value.protocol,
        port: value.port,
        host: value.host,
    };
}
