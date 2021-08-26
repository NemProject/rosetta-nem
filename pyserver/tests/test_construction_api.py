# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.construction_combine_request import ConstructionCombineRequest  # noqa: F401
from openapi_server.models.construction_combine_response import ConstructionCombineResponse  # noqa: F401
from openapi_server.models.construction_derive_request import ConstructionDeriveRequest  # noqa: F401
from openapi_server.models.construction_derive_response import ConstructionDeriveResponse  # noqa: F401
from openapi_server.models.construction_hash_request import ConstructionHashRequest  # noqa: F401
from openapi_server.models.construction_metadata_request import ConstructionMetadataRequest  # noqa: F401
from openapi_server.models.construction_metadata_response import ConstructionMetadataResponse  # noqa: F401
from openapi_server.models.construction_parse_request import ConstructionParseRequest  # noqa: F401
from openapi_server.models.construction_parse_response import ConstructionParseResponse  # noqa: F401
from openapi_server.models.construction_payloads_request import ConstructionPayloadsRequest  # noqa: F401
from openapi_server.models.construction_payloads_response import ConstructionPayloadsResponse  # noqa: F401
from openapi_server.models.construction_preprocess_request import ConstructionPreprocessRequest  # noqa: F401
from openapi_server.models.construction_preprocess_response import ConstructionPreprocessResponse  # noqa: F401
from openapi_server.models.construction_submit_request import ConstructionSubmitRequest  # noqa: F401
from openapi_server.models.error import Error  # noqa: F401
from openapi_server.models.transaction_identifier_response import TransactionIdentifierResponse  # noqa: F401


def test_construction_combine(client: TestClient):
    """Test case for construction_combine

    Create Network Transaction from Signatures
    """
    construction_combine_request = {"unsigned_transaction":"unsigned_transaction","signatures":[{"public_key":{"hex_bytes":"hex_bytes"},"signing_payload":{"address":"address","account_identifier":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"hex_bytes":"hex_bytes"},"hex_bytes":"hex_bytes"},{"public_key":{"hex_bytes":"hex_bytes"},"signing_payload":{"address":"address","account_identifier":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"hex_bytes":"hex_bytes"},"hex_bytes":"hex_bytes"}],"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/combine",
        headers=headers,
        json=construction_combine_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_derive(client: TestClient):
    """Test case for construction_derive

    Derive an AccountIdentifier from a PublicKey
    """
    construction_derive_request = {"public_key":{"hex_bytes":"hex_bytes"},"metadata":"{}","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/derive",
        headers=headers,
        json=construction_derive_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_hash(client: TestClient):
    """Test case for construction_hash

    Get the Hash of a Signed Transaction
    """
    construction_hash_request = {"signed_transaction":"signed_transaction","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/hash",
        headers=headers,
        json=construction_hash_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_metadata(client: TestClient):
    """Test case for construction_metadata

    Get Metadata for Transaction Construction
    """
    construction_metadata_request = {"public_keys":[{"hex_bytes":"hex_bytes"},{"hex_bytes":"hex_bytes"}],"options":"{}","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/metadata",
        headers=headers,
        json=construction_metadata_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_parse(client: TestClient):
    """Test case for construction_parse

    Parse a Transaction
    """
    construction_parse_request = {"signed":1,"transaction":"transaction","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/parse",
        headers=headers,
        json=construction_parse_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_payloads(client: TestClient):
    """Test case for construction_payloads

    Generate an Unsigned Transaction and Signing Payloads
    """
    construction_payloads_request = {"public_keys":[{"hex_bytes":"hex_bytes"},{"hex_bytes":"hex_bytes"}],"metadata":"{}","operations":[{"amount":{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"},"metadata":{"asm":"304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd01 03301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2","hex":"48304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd012103301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2"},"related_operations":[{"index":1},{"index":2}],"type":"Transfer","coin_change":{"coin_identifier":{"identifier":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1"}},"account":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"operation_identifier":{"index":5,"network_index":0},"status":"Reverted"},{"amount":{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"},"metadata":{"asm":"304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd01 03301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2","hex":"48304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd012103301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2"},"related_operations":[{"index":1},{"index":2}],"type":"Transfer","coin_change":{"coin_identifier":{"identifier":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1"}},"account":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"operation_identifier":{"index":5,"network_index":0},"status":"Reverted"}],"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/payloads",
        headers=headers,
        json=construction_payloads_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_preprocess(client: TestClient):
    """Test case for construction_preprocess

    Create a Request to Fetch Metadata
    """
    construction_preprocess_request = {"metadata":"{}","operations":[{"amount":{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"},"metadata":{"asm":"304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd01 03301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2","hex":"48304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd012103301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2"},"related_operations":[{"index":1},{"index":2}],"type":"Transfer","coin_change":{"coin_identifier":{"identifier":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1"}},"account":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"operation_identifier":{"index":5,"network_index":0},"status":"Reverted"},{"amount":{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"},"metadata":{"asm":"304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd01 03301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2","hex":"48304502201fd8abb11443f8b1b9a04e0495e0543d05611473a790c8939f089d073f90509a022100f4677825136605d732e2126d09a2d38c20c75946cd9fc239c0497e84c634e3dd012103301a8259a12e35694cc22ebc45fee635f4993064190f6ce96e7fb19a03bb6be2"},"related_operations":[{"index":1},{"index":2}],"type":"Transfer","coin_change":{"coin_identifier":{"identifier":"0x2f23fd8cca835af21f3ac375bac601f97ead75f2e79143bdf71fe2c4be043e8f:1"}},"account":{"metadata":"{}","address":"0x3a065000ab4183c6bf581dc1e55a605455fc6d61","sub_account":{"metadata":"{}","address":"0x6b175474e89094c44da98b954eedeac495271d0f"}},"operation_identifier":{"index":5,"network_index":0},"status":"Reverted"}],"suggested_fee_multiplier":0.08008281904610115,"max_fee":[{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"},{"metadata":"{}","currency":{"symbol":"BTC","metadata":{"issuer":"Satoshi"},"decimals":8},"value":"1238089899992"}],"network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/preprocess",
        headers=headers,
        json=construction_preprocess_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_construction_submit(client: TestClient):
    """Test case for construction_submit

    Submit a Signed Transaction
    """
    construction_submit_request = {"signed_transaction":"signed_transaction","network_identifier":{"blockchain":"bitcoin","sub_network_identifier":{"metadata":{"producer":"0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5"},"network":"shard 1"},"network":"mainnet"}}

    headers = {
    }
    response = client.request(
        "POST",
        "/construction/submit",
        headers=headers,
        json=construction_submit_request,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

