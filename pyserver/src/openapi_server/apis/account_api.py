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
from openapi_server.models.account_balance_request import AccountBalanceRequest
from openapi_server.models.account_balance_response import AccountBalanceResponse
from openapi_server.models.account_coins_request import AccountCoinsRequest
from openapi_server.models.account_coins_response import AccountCoinsResponse
from openapi_server.models.error import Error


router = APIRouter()


@router.post(
    "/account/balance",
    responses={
        200: {"model": AccountBalanceResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Account"],
    summary="Get an Account&#39;s Balance",
)
async def account_balance(
    account_balance_request: AccountBalanceRequest = Body(None, description=""),
) -> AccountBalanceResponse:
    """Get an array of all AccountBalances for an AccountIdentifier and the BlockIdentifier at which the balance lookup was performed. The BlockIdentifier must always be returned because some consumers of account balance data need to know specifically at which block the balance was calculated to compare balances they compute from operations with the balance returned by the node.  It is important to note that making a balance request for an account without populating the SubAccountIdentifier should not result in the balance of all possible SubAccountIdentifiers being returned. Rather, it should result in the balance pertaining to no SubAccountIdentifiers being returned (sometimes called the liquid balance). To get all balances associated with an account, it may be necessary to perform multiple balance requests with unique AccountIdentifiers.  It is also possible to perform a historical balance lookup (if the server supports it) by passing in an optional BlockIdentifier. """
    ...


@router.post(
    "/account/coins",
    responses={
        200: {"model": AccountCoinsResponse, "description": "Expected response to a valid request"},
        500: {"model": Error, "description": "unexpected error"},
    },
    tags=["Account"],
    summary="Get an Account&#39;s Unspent Coins",
)
async def account_coins(
    account_coins_request: AccountCoinsRequest = Body(None, description=""),
) -> AccountCoinsResponse:
    """Get an array of all unspent coins for an AccountIdentifier and the BlockIdentifier at which the lookup was performed. If your implementation does not support coins (i.e. it is for an account-based blockchain), you do not need to implement this endpoint. If you implementation does support coins (i.e. it is fro a UTXO-based blockchain), you MUST also complete the &#x60;/account/balance&#x60; endpoint.  It is important to note that making a coins request for an account without populating the SubAccountIdentifier should not result in the coins of all possible SubAccountIdentifiers being returned. Rather, it should result in the coins pertaining to no SubAccountIdentifiers being returned. To get all coins associated with an account, it may be necessary to perform multiple coin requests with unique AccountIdentifiers.  Optionally, an implementation may choose to support updating an AccountIdentifier&#39;s unspent coins based on the contents of the mempool. Note, using this functionality breaks any guarantee of idempotency. """
    ...
