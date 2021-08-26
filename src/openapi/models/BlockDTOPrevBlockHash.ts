/* tslint:disable */
/**
 *
 * @export
 * @interface BlockDTOPrevBlockHash
 */
export interface BlockDTOPrevBlockHash {
    /**
     *
     * @type {string}
     * @memberof BlockDTOPrevBlockHash
     */
    data: string;
}

export function BlockDTOPrevBlockHashFromJSON(json: any): BlockDTOPrevBlockHash {
    return BlockDTOPrevBlockHashFromJSONTyped(json, false);
}

export function BlockDTOPrevBlockHashFromJSONTyped(json: any, ignoreDiscriminator: boolean): BlockDTOPrevBlockHash {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        data: json['data'],
    };
}

export function BlockDTOPrevBlockHashToJSON(value?: BlockDTOPrevBlockHash | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        data: value.data,
    };
}
