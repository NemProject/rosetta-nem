# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.call_request import CallRequest  # noqa: F401
from openapi_server.models.call_response import CallResponse  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401


def test_call(client: TestClient):
    """Test case for call

    Make a Network-Specific Procedure Call
    """
    call_request = {"method":"eth_call","parameters":{"block_number":23,"address":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/call",
        headers=headers,
        json=call_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

