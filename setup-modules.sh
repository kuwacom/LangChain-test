#!/bin/bash
source venv/bin/activate

CMAKE_ARGS="-DLLAMA_CUDA=on"
FORCE_CMAKE=1
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir

pip install -r req.txt
