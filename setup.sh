#!/bin/bash

# Setup the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install all dependencies
pip3 install -r requirements.txt

echo "Setup completed. Use 'source venv/bin/activate' to activate the virtual environment."
