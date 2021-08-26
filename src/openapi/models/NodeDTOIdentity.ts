/* tslint:disable */
/**
 *
 * @export
 * @interface NodeDTOIdentity
 */
export interface NodeDTOIdentity {
    /**
     *
     * @type {string}
     * @memberof NodeDTOIdentity
     */
    name: string;
    /**
     *
     * @type {string}
     * @memberof NodeDTOIdentity
     */
    public_key: string;
}

export function NodeDTOIdentityFromJSON(json: any): NodeDTOIdentity {
    return NodeDTOIdentityFromJSONTyped(json, false);
}

export function NodeDTOIdentityFromJSONTyped(json: any, ignoreDiscriminator: boolean): NodeDTOIdentity {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        name: json['name'],
        public_key: json['public-key'],
    };
}

export function NodeDTOIdentityToJSON(value?: NodeDTOIdentity | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        name: value.name,
        'public-key': value.public_key,
    };
}
