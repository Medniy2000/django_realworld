#!/bin/bash

# Beautify project's code
python -m pip install --upgrade pip
echo "💥 Black formatter is checking.. ⏳ "
black .
echo "Black formatter finished! 💎"

echo "💥 Flake8 in checking.. ⏳ "
flake8 .
echo "Flake8 finished! 💎"

echo "💥 MyPy is checking.. ⏳ "
mypy .
echo "MyPy finished! 💎"