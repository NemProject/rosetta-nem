import { ModelError } from 'rosetta-sdk-typescript';

//REVISIT ALL THE ERRORS!
export class Errors {
    public static NETWORK_IDENTIFIER_IS_INVALID: ModelError = {
        code: 1106,
        message: 'Network identifier invalid',
        retriable: false,
    };

    public static BLOCK_HEIGHT_IS_REQUIRED: ModelError = {
        code: 1127,
        message: 'Block index (height) is required',
        retriable: false,
    };

    public static BLOCK_BY_HASH_IS_NOT_SUPPORTED: ModelError = {
        code: 1128,
        message: 'Block by hash is not supported',
        retriable: false,
    };

    public static INTERNAL_SERVER_ERROR: ModelError = {
        code: 500,
        message: 'Internal server error',
        retriable: false,
    };
    public static BAD_REQUEST: ModelError = {
        code: 1000,
        message: 'Bad request',
        retriable: false,
    };
    public static MODE_IS_OFFLINE: ModelError = {
        code: 1001,
        message: "Offline Mode can't support the api",
        retriable: false,
    };
    public static NODECONNETCONNECTION: ModelError = {
        code: 1002,
        message: 'Unable to connect node',
        retriable: false,
    };
    public static NODESYNCNOTCOMPLETE: ModelError = {
        code: 1003,
        message: 'Node synchronization is not complete',
        retriable: false,
    };
    public static NODEAPIERROR: ModelError = {
        code: 1004,
        message: 'Node api return error',
        retriable: false,
    };
    public static BLOCKNOTEXISTS: ModelError = {
        code: 1100,
        message: 'Block not exists',
        retriable: true,
    };
    public static TRANSACTIONNOTEXISTS: ModelError = {
        code: 1101,
        message: 'Transaction not exists',
        retriable: true,
    };
    public static SIGNEDTRANSACTIONINVALID: ModelError = {
        code: 1102,
        message: 'Signed Transaction is invalid',
        retriable: false,
    };

    public static PUBLICKEYPAYLOADINVALID: ModelError = {
        code: 1107,
        message: 'publickey info invalid',
        retriable: false,
    };
    public static TRANSACTIONISNOTHEX: ModelError = {
        code: 1108,
        message: 'transaction is not hex',
        retriable: false,
    };
    public static TRANSACTIONINVALID: ModelError = {
        code: 1109,
        message: 'transaction invalid',
        retriable: false,
    };
    public static TRANSACTIONNOTSUPPORT: ModelError = {
        code: 1110,
        message: 'the transaction type not support',
        retriable: false,
    };
    public static ABIDECODEERROR: ModelError = {
        code: 1111,
        message: 'ABI decode error',
        retriable: false,
    };
    public static OPERATIONINVALID: ModelError = {
        code: 1112,
        message: 'Operation array invalid',
        retriable: false,
    };
    public static METADATAINVALID: ModelError = {
        code: 1113,
        message: 'Metadata invalid',
        retriable: false,
    };
    public static NOSETORIGIN: ModelError = {
        code: 1114,
        message: 'No set transaction origin',
        retriable: false,
    };
    public static ORIGINSIGNTUREINVALID: ModelError = {
        code: 1115,
        message: 'the origin signature invalid',
        retriable: false,
    };
    public static DELEGATORSIGNATUREINVALID: ModelError = {
        code: 1116,
        message: 'the delegator signature invalid',
        retriable: false,
    };
    public static NOSETDELEGATORSINGTURE: ModelError = {
        code: 1117,
        message: 'noset delegator signature',
        retriable: false,
    };
    public static TRANSACTIONCHAINTAGINVALID: ModelError = {
        code: 1118,
        message: 'transaction chaintag invalid',
        retriable: false,
    };
    public static NETWORKIDENTIFIERINVALID: ModelError = {
        code: 1119,
        message: 'network_identifier invalid',
        retriable: false,
    };
    public static ACCOUNTIDENTIFIERINVALID: ModelError = {
        code: 1120,
        message: 'account_identifier invalid',
        retriable: false,
    };
    public static BLOCKIDENTIFIERINVALID: ModelError = {
        code: 1121,
        message: 'block_identifier invalid',
        retriable: false,
    };
    public static TRANSACTIONIDENTIFIERINVALID: ModelError = {
        code: 1122,
        message: 'transaction_identifier invalid',
        retriable: false,
    };
    public static MULTIORIGIN: ModelError = {
        code: 1123,
        message: 'No support multi orgin',
        retriable: false,
    };
    public static MULTIDELEGATOR: ModelError = {
        code: 1124,
        message: 'No support multi delegator',
        retriable: false,
    };
    public static OPERATIONSTOOMUCH: ModelError = {
        code: 1125,
        message: 'The operations too much',
        retriable: false,
    };
    public static CURRENCYINVALID: ModelError = {
        code: 1126,
        message: 'The currency invalid',
        retriable: false,
    };

    public static getErrors(): ModelError[] {
        return Object.getOwnPropertyNames(Errors)
            .filter((property) => ['length', 'prototype', 'name', 'getErrors'].indexOf(property) < 0)
            .map((property) => Errors[property]);
    }
}
