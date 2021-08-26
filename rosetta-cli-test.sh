#!/bin/bash
set -e

rosetta-cli check:data --configuration-file rosetta-cli-conf/testnet/config.json
rosetta-cli check:construction --configuration-file rosetta-cli-conf/testnet/config.json
