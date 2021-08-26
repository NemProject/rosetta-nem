git clone https://github.com/coinbase/rosetta-specifications
cd rosetta-specifications
openapi-generator-cli generate -g python-fastapi -i api.yaml -o ../pyserver
