#!/bin/bash
source venv/bin/activate

CMAKE_ARGS="-DLLAMA_CUBLAS=on"
FORCE_CMAKE=1

pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir

pip install -r req.txt
