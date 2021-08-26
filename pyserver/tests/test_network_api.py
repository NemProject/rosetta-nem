# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.metadata_request import MetadataRequest  # noqa: F401
from openapi_server.models.network_list_response import NetworkListResponse  # noqa: F401
from openapi_server.models.network_options_response import NetworkOptionsResponse  # noqa: F401
from openapi_server.models.network_request import NetworkRequest  # noqa: F401
from openapi_server.models.network_status_response import NetworkStatusResponse  # noqa: F401


def test_network_list(client: TestClient):
    """Test case for network_list

    Get List of Available Networks
    """
    metadata_request = {"metadata":"{}"}

    headers = {
    }
    response = client.request(
        "POST",
        "/network/list",
        headers=headers,
        json=metadata_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_network_options(client: TestClient):
    """Test case for network_options

    Get Network Options
    """
    network_request = {"metadata":"{}","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/network/options",
        headers=headers,
        json=network_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_network_status(client: TestClient):
    """Test case for network_status

    Get Network Status
    """
    network_request = {"metadata":"{}","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/network/status",
        headers=headers,
        json=network_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

