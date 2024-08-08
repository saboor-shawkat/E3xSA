#!/bin/bash

# Install required packages
pkg install git -y
pkg install python -y
pkg install python2 -y

# Clone the TBomb repository
git clone https://github.com/TheSpeedX/TBomb.git

# Change into the TBomb directory
cd TBomb

# Install the required Python packages
pip install -r requirements.txt

# Make the TBomb script executable
chmod +x TBomb.py

# Print a success message
echo "TBomb installed successfully! Run './TBomb.py' to start."
