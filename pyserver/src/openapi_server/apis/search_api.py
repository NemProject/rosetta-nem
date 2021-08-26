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
from openapi_server.models.search_transactions_request import SearchTransactionsRequest
from openapi_server.models.search_transactions_response import SearchTransactionsResponse


router = APIRouter()


@router.post(
    "/search/transactions",
    responses={
        200: {"model": SearchTransactionsResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Search"],
    summary="[INDEXER] Search for Transactions ",
)
async def search_transactions(
    search_transactions_request: SearchTransactionsRequest = Body(None, description=""),
) -> SearchTransactionsResponse:
    """&#x60;/search/transactions&#x60; allows the caller to search for transactions that meet certain conditions. Some conditions include matching a transaction hash, containing an operation with a certain status, or containing an operation that affects a certain account.  &#x60;/search/transactions&#x60; is considered an \&quot;indexer\&quot; endpoint and Rosetta implementations are not required to complete it to adhere to the Rosetta spec. However, any Rosetta \&quot;indexer\&quot; MUST support this endpoint. """
    ...
