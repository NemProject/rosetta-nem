# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.mempool_response import MempoolResponse  # noqa: F401
from openapi_server.models.mempool_transaction_request import MempoolTransactionRequest  # noqa: F401
from openapi_server.models.mempool_transaction_response import MempoolTransactionResponse  # noqa: F401
from openapi_server.models.network_request import NetworkRequest  # noqa: F401


def test_mempool(client: TestClient):
    """Test case for mempool

    Get All Mempool Transactions
    """
    network_request = {"metadata":"{}","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/mempool",
        headers=headers,
        json=network_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_mempool_transaction(client: TestClient):
    """Test case for mempool_transaction

    Get a Mempool Transaction
    """
    mempool_transaction_request = {"transaction_identifier":{"hash":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f"},"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/mempool/transaction",
        headers=headers,
        json=mempool_transaction_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

