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
from openapi_server.models.metadata_request import MetadataRequest
from openapi_server.models.network_list_response import NetworkListResponse
from openapi_server.models.network_options_response import NetworkOptionsResponse
from openapi_server.models.network_request import NetworkRequest
from openapi_server.models.network_status_response import NetworkStatusResponse

from openapi_server.models.allow import Allow
from openapi_server.models.block_identifier import BlockIdentifier
from openapi_server.models.network_identifier import NetworkIdentifier
from openapi_server.models.peer import Peer
from openapi_server.models.sync_status import SyncStatus
from openapi_server.models.version import Version

router = APIRouter()


@router.post(
    "/network/list",
    responses={
        200: {"model": NetworkListResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Network"],
    summary="Get List of Available Networks",
)
async def network_list(
    metadata_request: MetadataRequest = Body(None, description=""),
) -> NetworkListResponse:
    """This endpoint returns a list of NetworkIdentifiers that the Rosetta server supports. """
    return NetworkListResponse(
        network_identifiers=[
            NetworkIdentifier(blockchain='NEM', network='mainnet')
        ]
    )


@router.post(
    "/network/options",
    responses={
        200: {"model": NetworkOptionsResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Network"],
    summary="Get Network Options",
)
async def network_options(
    network_request: NetworkRequest = Body(None, description=""),
) -> NetworkOptionsResponse:
    """This endpoint returns the version information and allowed network-specific types for a NetworkIdentifier. Any NetworkIdentifier returned by /network/list should be accessible here.  Because options are retrievable in the context of a NetworkIdentifier, it is possible to define unique options for each network. """
    return NetworkOptionsResponse(
        version=Version(
            rosetta_version='1.0.0',
            node_version='123',

        ),
        allow=Allow(
            operation_statuses=[
                {
                    "status": "SUCCESS",
                    "successful": True
                }
            ],
            operation_types=[
                "TRANSFER"
            ],
            errors=[],
            historical_balance_lookup=False,
            timestamp_start_index=1,
            call_methods=[],
            balance_exemptions=[],
            mempool_coins=False # ...
        )
    )


@router.post(
    "/network/status",
    responses={
        200: {"model": NetworkStatusResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Network"],
    summary="Get Network Status",
)
async def network_status(
    network_request: NetworkRequest = Body(None, description=""),
) -> NetworkStatusResponse:
    """This endpoint returns the current status of the network requested. Any NetworkIdentifier returned by /network/list should be accessible here. """
    if network_request.network_identifier != NetworkIdentifier(blockchain='NEM', network='mainnet'):
        return Error(code=1, message='invalid network', retriable=True)

    current_block_identifier=BlockIdentifier(
        index = 1,
        hash = '1234567890abcdef'
    )
    genesis_block_identifier=BlockIdentifier(
        index = 1,
        hash = '1234567890abcdef'
    )

    return NetworkStatusResponse(
        current_block_identifier=current_block_identifier,
        current_block_timestamp=1615853185000,
        genesis_block_identifier=genesis_block_identifier,
        #oldest_block_identifier=
        sync_status=SyncStatus(
                current_index=1,
                target_index=0,
                synced=True
        ),
        peers=[
        ]
    )
