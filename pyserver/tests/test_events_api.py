# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.events_blocks_request import EventsBlocksRequest  # noqa: F401
from openapi_server.models.events_blocks_response import EventsBlocksResponse  # noqa: F401


def test_events_blocks(client: TestClient):
    """Test case for events_blocks

    [INDEXER] Get a range of BlockEvents 
    """
    events_blocks_request = {"offset":5,"limit":5,"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/events/blocks",
        headers=headers,
        json=events_blocks_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

