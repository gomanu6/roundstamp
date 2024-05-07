#!/bin/bash

. ./stamp_pages.config

folder=${folder_pdf}







### Handing over to Python
echo "${p} Local Installed Python Version is: $(python3 --version)"

python3 -m venv "${python_env_name}"
source "${python_env_name}/bin/activate"
pip install --upgrade pymupdf

python3 stamp_pages.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${images_folder}"


# pip3 freeze > requirements.txt
deactivate
### Back to Bash




