#!/bin/bash
set -e

# Specify the name of the new environment
ENV_NAME="env_money_laundering"

# Specify Python version
PYTHON_VERSION="3.8"

# Path to the requirements.txt file
REQUIREMENTS_FILE="requirements.txt"


handle_error() {
    echo "An error occurred: $1"
    # Additional error handling code can go here
}
# Set the error handler to be called when an error occurs
trap 'handle_error "Something went wrong!"' ERR

echo "Creating a new Anaconda environment named $ENV_NAME with Python $PYTHON_VERSION..."
conda create --name $ENV_NAME python=$PYTHON_VERSION -y

# Activate the new environment
echo "Activating the new environment..."
source activate $ENV_NAME

# Install dependencies
# Check if the requirements.txt file exists and install dependencies
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "Error: $REQUIREMENTS_FILE does not exist."
    exit 1
fi

python script.py

echo "Environment setup complete. $ENV_NAME is ready to use!"
