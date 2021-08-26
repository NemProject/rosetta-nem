/* tslint:disable */
/**
 *
 * @export
 * @interface ChainScoreDTO
 */
export interface ChainScoreDTO {
    /**
     *
     * @type {string}
     * @memberof ChainScoreDTO
     */
    score: string;
}

export function ChainScoreDTOFromJSON(json: any): ChainScoreDTO {
    return ChainScoreDTOFromJSONTyped(json, false);
}

export function ChainScoreDTOFromJSONTyped(json: any, ignoreDiscriminator: boolean): ChainScoreDTO {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        score: json['score'],
    };
}

export function ChainScoreDTOToJSON(value?: ChainScoreDTO | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        score: value.score,
    };
}
