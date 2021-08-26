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
    ...


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
    ...


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
    ...
