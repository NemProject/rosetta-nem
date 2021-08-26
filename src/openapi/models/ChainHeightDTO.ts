/* tslint:disable */
/**
 *
 * @export
 * @interface ChainHeightDTO
 */
export interface ChainHeightDTO {
    /**
     *
     * @type {number}
     * @memberof ChainHeightDTO
     */
    height: number;
}

export function ChainHeightDTOFromJSON(json: any): ChainHeightDTO {
    return ChainHeightDTOFromJSONTyped(json, false);
}

export function ChainHeightDTOFromJSONTyped(json: any, ignoreDiscriminator: boolean): ChainHeightDTO {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        height: json['height'],
    };
}

export function ChainHeightDTOToJSON(value?: ChainHeightDTO | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        height: value.height,
    };
}
