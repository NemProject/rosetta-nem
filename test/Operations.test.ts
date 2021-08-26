import 'chai';
import { expect } from 'chai';
import 'mocha';
import { Operations, OperationStatusObjects } from 'rosetta-nem';

describe('Operations', () => {
    it('getOperations', () => {
        expect(Operations.getOperations()).deep.eq([
            'TRANSFER_257',
            'TRANSFER_OF_IMPORTANCE_2049',
            'AGGREGATE_MODIFICATION_4097',
            'MULTISIG_SIGNATURE_4098',
            'MULTISIG_4099',
        ]);
    });

    it('getStatusList', () => {
        expect(OperationStatusObjects.getStatusList()).deep.eq([
            {
                status: 'None',
                successful: false,
            },
            {
                status: 'Pending',
                successful: false,
            },
            {
                status: 'Reverted',
                successful: false,
            },
            {
                status: 'Succeeded',
                successful: true,
            },
        ]);
    });
});
