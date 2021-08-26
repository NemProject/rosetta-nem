/* tslint:disable */
/**
 *
 * @export
 * @interface BlockAtPublicRequestDTO
 */
export interface BlockAtPublicRequestDTO {
    /**
     *
     * @type {number}
     * @memberof BlockAtPublicRequestDTO
     */
    height: number;
}

export function BlockAtPublicRequestDTOFromJSON(json: any): BlockAtPublicRequestDTO {
    return BlockAtPublicRequestDTOFromJSONTyped(json, false);
}

export function BlockAtPublicRequestDTOFromJSONTyped(json: any, ignoreDiscriminator: boolean): BlockAtPublicRequestDTO {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        height: json['height'],
    };
}

export function BlockAtPublicRequestDTOToJSON(value?: BlockAtPublicRequestDTO | null): any {
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
