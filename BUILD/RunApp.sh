#!/bin/bash

PYTHON_EXE_PATH=

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

for word in $*; do echo "$word"; done

LIB_PATH="${SCRIPT_DIR}/LIB" \
PYTHONPATH=$SCRIPT_DIR \
"${PYTHON_EXE_PATH}python3" -O $SCRIPT_DIR/MyPyTalks.pyz --env $SCRIPT_DIR/.env $*