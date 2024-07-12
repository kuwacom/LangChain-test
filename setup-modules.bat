@echo off
call .\venv\Scripts\activate

set CMAKE_ARGS="-DLLAMA_CUBLAS=on"
set FORCE_CMAKE=1

pip install --upgrade --force-reinstall llama-cpp-python --no-cache-dir
pip install -r req.txt