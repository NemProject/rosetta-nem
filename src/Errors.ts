import { ModelError } from 'rosetta-sdk-typescript';

export class Errors {
    public static NETWORK_IDENTIFIER_IS_INVALID: ModelError = {
        code: 1000,
        message: 'Network identifier invalid',
        retriable: false,
    };

    public static getErrors(): ModelError[] {
        return Object.getOwnPropertyNames(Errors)
            .filter((property) => ['length', 'prototype', 'name', 'getErrors'].indexOf(property) < 0)
            .map((property) => Errors[property]);
    }
}
