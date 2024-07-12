@echo off
call .\venv\Scripts\activate

set CMAKE_ARGS="-DLLAMA_CUDA=on"
set FORCE_CMAKE=1
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir

pip install -r req.txt