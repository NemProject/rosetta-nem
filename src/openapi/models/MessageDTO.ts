/* tslint:disable */
/**
 *
 * @export
 * @interface MessageDTO
 */
export interface MessageDTO {
    /**
     *
     * @type {string}
     * @memberof MessageDTO
     */
    payload: string;
    /**
     *
     * @type {number}
     * @memberof MessageDTO
     */
    type: number;
}

export function MessageDTOFromJSON(json: any): MessageDTO {
    return MessageDTOFromJSONTyped(json, false);
}

export function MessageDTOFromJSONTyped(json: any, ignoreDiscriminator: boolean): MessageDTO {
    if (json === undefined || json === null) {
        return json;
    }
    return {
        payload: json['payload'],
        type: json['type'],
    };
}

export function MessageDTOToJSON(value?: MessageDTO | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        payload: value.payload,
        type: value.type,
    };
}
