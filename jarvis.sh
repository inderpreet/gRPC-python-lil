#!/bin/bash

if [[ $# -ne 1 ]]; then
        echo "Illegal number of params"
        echo "setup pip-install to setup deps"
        echo "setup pip-freeze to generate requirements.txt"
        exit -1
elif [[ "$1" == "pip-install" ]]; then
        echo "Installing..."
        source ./venv/bin/activate
        pip install -r requirements.txt
elif [[ "$1" == "pip-freeze" ]]; then
        echo "Freezing..."
        source ./venv/bin/activate
        pip freeze > requirements.txt
elif [[ "$1" == "gen" ]]; then
        protoc --python_out=. rides.proto
elif [[ "$1" == "gen2" ]]; then        
        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. rides.proto
elif [[ "$1" == "cleanup" ]]; then
        rm ./rides_pb2.py
        rm rides_pb2_grpc.py
elif [[ "$1" == "run" ]]; then
        python main.py
else
        echo "unknown operation. Check spellings"
fi
# pip install -r requirements.txt
# pip freeze > requirements.txt
