# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.search_transactions_request import SearchTransactionsRequest  # noqa: F401
from openapi_server.models.search_transactions_response import SearchTransactionsResponse  # noqa: F401


def test_search_transactions(client: TestClient):
    """Test case for search_transactions

    [INDEXER] Search for Transactions 
    """
    search_transactions_request = {"address":"0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347","offset":5,"max_block":5,"account_identifier":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"coin_identifier":{"identifier":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1"},"type":"transfer","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"},"transaction_identifier":{"hash":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f"},"success":1,"limit":5,"currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"status":"reverted"}

    headers = {
    }
    response = client.request(
        "POST",
        "/search/transactions",
        headers=headers,
        json=search_transactions_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

