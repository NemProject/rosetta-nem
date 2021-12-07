import 'chai';
import { expect } from 'chai';
import 'mocha';
import { Errors } from 'rosetta-nem';

describe('Errors', () => {
    it('getOperations', () => {
        expect(Errors.getErrors()).deep.eq([Errors.NETWORK_IDENTIFIER_IS_INVALID]);
    });
});
