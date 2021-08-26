# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.block_request import BlockRequest  # noqa: F401
from openapi_server.models.block_response import BlockResponse  # noqa: F401
from openapi_server.models.block_transaction_request import BlockTransactionRequest  # noqa: F401
from openapi_server.models.block_transaction_response import BlockTransactionResponse  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_block(client: TestClient):
    """Test case for block

    Get a Block
    """
    block_request = {"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"},"block_identifier":{"index":1123941,"hash":"0x1f2cc6c5027d2f201a5453ad1119574d2aed23a392654742ac3c78783c071f85"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/block",
        headers=headers,
        json=block_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_block_transaction(client: TestClient):
    """Test case for block_transaction

    Get a Block Transaction
    """
    block_transaction_request = {"transaction_identifier":{"hash":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f"},"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"},"block_identifier":{"index":1123941,"hash":"0x1f2cc6c5027d2f201a5453ad1119574d2aed23a392654742ac3c78783c071f85"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/block/transaction",
        headers=headers,
        json=block_transaction_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

