import { OperationStatus } from 'rosetta-sdk-typescript';

//List the different operations, are one per transaction type? Use the SDK values!
export enum TransactionType {
    //Transfer of NEM from sender to recipient.
    TRANSFER = 0x101,

    //Transfer of importance from sender to remote account.
    TRANSFER_OF_IMPORTANCE = 0x801,

    //An aggregate modification transaction, which converts a normal account into a multisig account.
    AGGREGATE_MODIFICATION = 0x1001,

    //A multisig signature transaction which is used to sign a multisig transaction.
    MULTISIG_SIGNATURE = 0x1002,

    // A multisig transaction, which is used for multisig accounts.
    MULTISIG = 0x1003,
}

export class Operations {
    public static getOperations(): string[] {
        return Object.values(TransactionType)
            .filter((transactionType) => parseInt(transactionType.toString()))
            .map((transactionType) => this.toOperation(transactionType as TransactionType));
    }

    public static toOperation(transactionType: TransactionType) {
        return `${TransactionType[transactionType]}_${transactionType}`;
    }
}

// List the different status
export class OperationStatusObjects {
    public static None: OperationStatus = { status: 'None', successful: false };
    public static Pending: OperationStatus = {
        status: 'Pending',
        successful: false,
    };
    public static Reverted: OperationStatus = {
        status: 'Reverted',
        successful: false,
    };
    public static Succeeded: OperationStatus = {
        status: 'Succeeded',
        successful: true,
    };

    public static getStatusList(): OperationStatus[] {
        return Object.getOwnPropertyNames(OperationStatusObjects)
            .filter((property) => ['length', 'prototype', 'name', 'getStatusList'].indexOf(property) < 0)
            .map((property) => OperationStatusObjects[property]);
    }
}
