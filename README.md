# NEM Rosetta implementation

Implementation Rosetta Spec for NEM Network.

[![License](https://img.shields.io/npm/l/rosetta-nem.svg)](https://github.com/NemProject/rosetta-nem/blob/main/package.json)
[![Build Status](https://travis-ci.com/NemProject/rosetta-nem.svg?branch=main)](https://travis-ci.com/NemProject/rosetta-nem)
[![Coverage Status](https://coveralls.io/repos/github/NemProject/rosetta-nem/badge.svg?branch=main)](https://coveralls.io/github/NemProject/rosetta-nem?branch=main)
[![Api Doc](https://img.shields.io/badge/api-doc-blue.svg)](https://NemProject.github.io/rosetta-nem/)


## Overview

Typescript implementation of the Rosetta API for the NEM Network. This implementation uses Fernando's [rosetta-sdk-typescript](https://github.com/fboucquez/rosetta-sdk-typescript).

## NEM Open API

The communication between the Rosetta Service and NEM's Rest is done via OpenApi Generated clients. The generated code is located in `src/openapi`.

Note: this is not the Rosetta generate server and client. The  [rosetta-sdk-typescript](https://github.com/fboucquez/rosetta-sdk-typescript) provides and maintain them.


## Development (Current).

Clone the repo

````commandline
git clone https://github.com/NemProject/rosetta-nem.git
cd rosetta-nem
npm install
npm run dev
````

A Rosetta Server wills tart in port 8080. This Server talks to testnet's HugeAlice.
It's possible to swap HugeAlice with a local node using program arguments.

You can query some basic endpoints like `/network/list`, `/network/options`, `/network/status`, `/block`, etc.

TODO: All endpoints need to be revisited, they are either POC endpoints or placeholders for the implementation.

Other useful commands:

* `npm run openapi:gen` to generate NEM Rest client from the (In Progress) NEM Open API specification.
* `npm test` to run tests
* `npm doc` to generate the docs.
* `npm style:fix` to pretty, index, and lint the source code (including generated code)

## Packages
* [OpenApi](src/openapi): Auto-generated NEM types and NEM Rest client. DO NOT modify this folder.
* [Client](src/client): NEM rest client factory, that creates Main class is `NemRestClientFactory`.
* [Services](src/services): Implementation of the services the Rosetta SDK's controller will use and expose.
* [RosettaNem.ts](src/RosettaNem.ts): The main class that runs the Rosetta server.

## Test

Testing options are:

- Regular unit test using Mocha and Chai. Run `npm run test`
- Integration test using Mocha and Chai. Run `npm run test:e2e`
- Integration test using rosetta-cli. Run `rosetta-cli-test.sh` while the Rosetta service is running.

## Architecture

TODO

## Building the Image

TODO

## Running the Image

TODO

## System Requirements

TODO

