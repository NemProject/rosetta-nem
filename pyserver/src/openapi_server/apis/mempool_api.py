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
from openapi_server.models.mempool_response import MempoolResponse
from openapi_server.models.mempool_transaction_request import MempoolTransactionRequest
from openapi_server.models.mempool_transaction_response import MempoolTransactionResponse
from openapi_server.models.network_request import NetworkRequest


router = APIRouter()


@router.post(
    "/mempool",
    responses={
        200: {"model": MempoolResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Mempool"],
    summary="Get All Mempool Transactions",
)
async def mempool(
    network_request: NetworkRequest = Body(None, description=""),
) -> MempoolResponse:
    """Get all Transaction Identifiers in the mempool"""
    ...


@router.post(
    "/mempool/transaction",
    responses={
        200: {"model": MempoolTransactionResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Mempool"],
    summary="Get a Mempool Transaction",
)
async def mempool_transaction(
    mempool_transaction_request: MempoolTransactionRequest = Body(None, description=""),
) -> MempoolTransactionResponse:
    """Get a transaction in the mempool by its Transaction Identifier. This is a separate request than fetching a block transaction (/block/transaction) because some blockchain nodes need to know that a transaction query is for something in the mempool instead of a transaction in a block.  Transactions may not be fully parsable until they are in a block (ex: may not be possible to determine the fee to pay before a transaction is executed). On this endpoint, it is ok that returned transactions are only estimates of what may actually be included in a block. """
    ...
