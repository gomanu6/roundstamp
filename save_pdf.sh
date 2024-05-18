#!/bin/bash

. ./save_pdf.config

link=$1


# apt install wkhtmltopdf

### Handing over to Python
echo
echo "${p} Local Installed Python Version is: $(python3 --version)"
echo

echo "---> Handing over to Python"
python3 -m venv "${python_env_name}"
source "${python_env_name}/bin/activate"
pip install "${python_modules}"

echo

python3 save_pdf.py "${link}" 

# pip3 freeze > requirements.txt
deactivate


### Back to Bash


