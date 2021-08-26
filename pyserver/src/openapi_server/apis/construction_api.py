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
from openapi_server.models.construction_combine_request import ConstructionCombineRequest
from openapi_server.models.construction_combine_response import ConstructionCombineResponse
from openapi_server.models.construction_derive_request import ConstructionDeriveRequest
from openapi_server.models.construction_derive_response import ConstructionDeriveResponse
from openapi_server.models.construction_hash_request import ConstructionHashRequest
from openapi_server.models.construction_metadata_request import ConstructionMetadataRequest
from openapi_server.models.construction_metadata_response import ConstructionMetadataResponse
from openapi_server.models.construction_parse_request import ConstructionParseRequest
from openapi_server.models.construction_parse_response import ConstructionParseResponse
from openapi_server.models.construction_payloads_request import ConstructionPayloadsRequest
from openapi_server.models.construction_payloads_response import ConstructionPayloadsResponse
from openapi_server.models.construction_preprocess_request import ConstructionPreprocessRequest
from openapi_server.models.construction_preprocess_response import ConstructionPreprocessResponse
from openapi_server.models.construction_submit_request import ConstructionSubmitRequest
from openapi_server.models.error import Error
from openapi_server.models.transaction_identifier_response import TransactionIdentifierResponse


router = APIRouter()


@router.post(
    "/construction/combine",
    responses={
        200: {"model": ConstructionCombineResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Create Network Transaction from Signatures",
)
async def construction_combine(
    construction_combine_request: ConstructionCombineRequest = Body(None, description=""),
) -> ConstructionCombineResponse:
    """Combine creates a network-specific transaction from an unsigned transaction and an array of provided signatures.  The signed transaction returned from this method will be sent to the &#x60;/construction/submit&#x60; endpoint by the caller. """
    ...


@router.post(
    "/construction/derive",
    responses={
        200: {"model": ConstructionDeriveResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Derive an AccountIdentifier from a PublicKey",
)
async def construction_derive(
    construction_derive_request: ConstructionDeriveRequest = Body(None, description=""),
) -> ConstructionDeriveResponse:
    """Derive returns the AccountIdentifier associated with a public key.  Blockchains that require an on-chain action to create an account should not implement this method. """
    ...


@router.post(
    "/construction/hash",
    responses={
        200: {"model": TransactionIdentifierResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Get the Hash of a Signed Transaction",
)
async def construction_hash(
    construction_hash_request: ConstructionHashRequest = Body(None, description=""),
) -> TransactionIdentifierResponse:
    """TransactionHash returns the network-specific transaction hash for a signed transaction. """
    ...


@router.post(
    "/construction/metadata",
    responses={
        200: {"model": ConstructionMetadataResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Get Metadata for Transaction Construction",
)
async def construction_metadata(
    construction_metadata_request: ConstructionMetadataRequest = Body(None, description=""),
) -> ConstructionMetadataResponse:
    """Get any information required to construct a transaction for a specific network. Metadata returned here could be a recent hash to use, an account sequence number, or even arbitrary chain state. The request used when calling this endpoint is created by calling &#x60;/construction/preprocess&#x60; in an offline environment.  You should NEVER assume that the request sent to this endpoint will be created by the caller or populated with any custom parameters. This must occur in &#x60;/construction/preprocess&#x60;.  It is important to clarify that this endpoint should not pre-construct any transactions for the client (this should happen in &#x60;/construction/payloads&#x60;). This endpoint is left purposely unstructured because of the wide scope of metadata that could be required. """
    ...


@router.post(
    "/construction/parse",
    responses={
        200: {"model": ConstructionParseResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Parse a Transaction",
)
async def construction_parse(
    construction_parse_request: ConstructionParseRequest = Body(None, description=""),
) -> ConstructionParseResponse:
    """Parse is called on both unsigned and signed transactions to understand the intent of the formulated transaction.  This is run as a sanity check before signing (after &#x60;/construction/payloads&#x60;) and before broadcast (after &#x60;/construction/combine&#x60;).  """
    ...


@router.post(
    "/construction/payloads",
    responses={
        200: {"model": ConstructionPayloadsResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Generate an Unsigned Transaction and Signing Payloads",
)
async def construction_payloads(
    construction_payloads_request: ConstructionPayloadsRequest = Body(None, description=""),
) -> ConstructionPayloadsResponse:
    """Payloads is called with an array of operations and the response from &#x60;/construction/metadata&#x60;. It returns an unsigned transaction blob and a collection of payloads that must be signed by particular AccountIdentifiers using a certain SignatureType.  The array of operations provided in transaction construction often times can not specify all \&quot;effects\&quot; of a transaction (consider invoked transactions in Ethereum). However, they can deterministically specify the \&quot;intent\&quot; of the transaction, which is sufficient for construction. For this reason, parsing the corresponding transaction in the Data API (when it lands on chain) will contain a superset of whatever operations were provided during construction. """
    ...


@router.post(
    "/construction/preprocess",
    responses={
        200: {"model": ConstructionPreprocessResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Create a Request to Fetch Metadata",
)
async def construction_preprocess(
    construction_preprocess_request: ConstructionPreprocessRequest = Body(None, description=""),
) -> ConstructionPreprocessResponse:
    """Preprocess is called prior to &#x60;/construction/payloads&#x60; to construct a request for any metadata that is needed for transaction construction given (i.e. account nonce).  The &#x60;options&#x60; object returned from this endpoint will be sent to the &#x60;/construction/metadata&#x60; endpoint UNMODIFIED by the caller (in an offline execution environment). If your Construction API implementation has configuration options, they MUST be specified in the &#x60;/construction/preprocess&#x60; request (in the &#x60;metadata&#x60; field). """
    ...


@router.post(
    "/construction/submit",
    responses={
        200: {"model": TransactionIdentifierResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Construction"],
    summary="Submit a Signed Transaction",
)
async def construction_submit(
    construction_submit_request: ConstructionSubmitRequest = Body(None, description=""),
) -> TransactionIdentifierResponse:
    """Submit a pre-signed transaction to the node. This call should not block on the transaction being included in a block. Rather, it should return immediately with an indication of whether or not the transaction was included in the mempool.  The transaction submission response should only return a 200 status if the submitted transaction could be included in the mempool. Otherwise, it should return an error. """
    ...
