#!/bin/bash
export PYTHONPATH=$(pwd)
python -B samples/$1.py

# Usage:
#   sample.sh [name]

# Example:
#   sample.sh javaFile