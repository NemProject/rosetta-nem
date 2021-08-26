# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from openapi_server.models.error import Error
from openapi_server.models.events_blocks_request import EventsBlocksRequest
from openapi_server.models.events_blocks_response import EventsBlocksResponse


router = APIRouter()


@router.post(
    "/events/blocks",
    responses={
        200: {"model": EventsBlocksResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Events"],
    summary="[INDEXER] Get a range of BlockEvents ",
)
async def events_blocks(
    events_blocks_request: EventsBlocksRequest = Body(None, description=""),
) -> EventsBlocksResponse:
    """&#x60;/events/blocks&#x60; allows the caller to query a sequence of BlockEvents indicating which blocks were added and removed from storage to reach the current state. Following BlockEvents allows lightweight clients to update their state without needing to implement their own syncing logic (like finding the common parent in a reorg).  &#x60;/events/blocks&#x60; is considered an \&quot;indexer\&quot; endpoint and Rosetta implementations are not required to complete it to adhere to the Rosetta spec. However, any Rosetta \&quot;indexer\&quot; MUST support this endpoint. """
    ...
