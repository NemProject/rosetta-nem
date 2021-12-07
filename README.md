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

Other useful commands:

* `npm test` to run tests
* `npm doc` to generate the docs.
* `npm style:fix` to pretty, index, and lint the source code (including generated code)

## Packages
* [Services](src/services): Implementation of the services the Rosetta SDK's controller will use and expose.
* [RosettaNem.ts](src/RosettaNem.ts): The main class that runs the Rosetta server.

## Test

Testing options are:

- Regular unit test using Mocha and Chai. Run `npm run test`
- Integration test using Mocha and Chai. Run `npm run test:e2e`

## Architecture

TODO

## Building the Image

TODO

## Running the Image

TODO

## System Requirements

TODO

