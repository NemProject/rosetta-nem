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
from openapi_server.models.block_request import BlockRequest
from openapi_server.models.block_response import BlockResponse
from openapi_server.models.block_transaction_request import BlockTransactionRequest
from openapi_server.models.block_transaction_response import BlockTransactionResponse
from openapi_server.models.error import Error


router = APIRouter()


@router.post(
    "/block",
    responses={
        200: {"model": BlockResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Block"],
    summary="Get a Block",
)
async def block(
    block_request: BlockRequest = Body(None, description=""),
) -> BlockResponse:
    """Get a block by its Block Identifier. If transactions are returned in the same call to the node as fetching the block, the response should include these transactions in the Block object. If not, an array of Transaction Identifiers should be returned so /block/transaction fetches can be done to get all transaction information.  When requesting a block by the hash component of the BlockIdentifier, this request MUST be idempotent: repeated invocations for the same hash-identified block must return the exact same block contents.  No such restriction is imposed when requesting a block by height, given that a chain reorg event might cause the specific block at height &#x60;n&#x60; to be set to a different one. """
    ...


@router.post(
    "/block/transaction",
    responses={
        200: {"model": BlockTransactionResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Block"],
    summary="Get a Block Transaction",
)
async def block_transaction(
    block_transaction_request: BlockTransactionRequest = Body(None, description=""),
) -> BlockTransactionResponse:
    """Get a transaction in a block by its Transaction Identifier. This endpoint should only be used when querying a node for a block does not return all transactions contained within it.  All transactions returned by this endpoint must be appended to any transactions returned by the /block method by consumers of this data. Fetching a transaction by hash is considered an Explorer Method (which is classified under the Future Work section).  This method can be used to let consumers to paginate results when the  block trasactions count is too big to be returned in a single BlockResponse.  Calling this endpoint requires reference to a BlockIdentifier because transaction parsing can change depending on which block contains the transaction. For example, in Bitcoin it is necessary to know which block contains a transaction to determine the destination of fee payments. Without specifying a block identifier, the node would have to infer which block to use (which could change during a re-org).  Implementations that require fetching previous transactions to populate the response (ex: Previous UTXOs in Bitcoin) may find it useful to run a cache within the Rosetta server in the /data directory (on a path that does not conflict with the node). """
    ...
