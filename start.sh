#!/bin/bash


echo "Hello from Bash"

# timedatectl set-timezone Asia/Kolkata

# apt update
# apt install -y python3 python3-venv python3-pip zip unzip vim dos2unix

# cp -r /input /output/ 

echo "Local Installed Python Version is: $(python3 --version)"

# python3 -m venv "py2"
# source "/app/py2/bin/activate"
# pip install --upgrade pymupdf

# python3 /app/rs.py

## Convert to Unix Format if Required
# dos2unix /app/*.sh
# dos2unix /app/*.py
# dos2unix /app/*.config
# dos2unix /app/*/*.sh
# dos2unix /app/*/*.config
# dos2unix /app/*/*.py


## Make executable
# chmod +x /app/*.sh


bash /app/docker_stamp.sh