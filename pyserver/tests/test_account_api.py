# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.account_balance_request import AccountBalanceRequest  # noqa: F401
from openapi_server.models.account_balance_response import AccountBalanceResponse  # noqa: F401
from openapi_server.models.account_coins_request import AccountCoinsRequest  # noqa: F401
from openapi_server.models.account_coins_response import AccountCoinsResponse  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_account_balance(client: TestClient):
    """Test case for account_balance

    Get an Account's Balance
    """
    account_balance_request = {"account_identifier":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"},"block_identifier":{"index":1123941,"hash":"0x1f2cc6c5027d2f201a5453ad1119574d2aed23a392654742ac3c78783c071f85"},"currencies":[{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8}]}

    headers = {
    }
    response = client.request(
        "POST",
        "/account/balance",
        headers=headers,
        json=account_balance_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_account_coins(client: TestClient):
    """Test case for account_coins

    Get an Account's Unspent Coins
    """
    account_coins_request = {"account_identifier":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"include_mempool":1,"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"},"currencies":[{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8}]}

    headers = {
    }
    response = client.request(
        "POST",
        "/account/coins",
        headers=headers,
        json=account_coins_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

