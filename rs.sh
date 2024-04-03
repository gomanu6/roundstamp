#!/bin/bash

# unstamped_zipfile=$1

n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)

. ./rs.config

base_folder="${data_folder}"

stamps_folder="${base_folder}/${stamps_folder_name}"
stamp_file="${stamps_folder}/${stamp_filename}"

unstamped_folder="${base_folder}/${unstamped_folder_name}"
stamped_folder="${base_folder}/${stamped_folder_name}"

final_folder="${base_folder}/${final_folder_name}"


unstamped_zipfile="${annexure_file}"
tmp_unzip_folder="${base_folder}/${tmp_unzip_folder_name}"

echo "${p} Deleting Old Data Folder"
rm -rf "${base_folder}"


# if [ "$#" -le 0 ]; then
#     echo "${p} File not specified"
#     exit 1
# fi

echo "${p} Checking if file exists"
if [ -f "${unstamped_zipfile}" ]; then
    
    o_user=$(stat -c %U "${unstamped_zipfile}")
    o_group=$(stat -c %G "${unstamped_zipfile}")
    zip_filename=$(basename "${unstamped_zipfile}")
    y=${zip_filename%.*}
    echo "${y}"
    path_to_replace="${unstamped_folder}/${y}"
    echo "${p} File exists and has username as ${o_user} and group as ${o_group}"
else
    echo "${p} File does not exist"
    echo "${p} exiting .. "
    exit 1
fi

if [ -d "${base_folder}" ]; then
    echo "${p} Data folder exists. Making Stamped and Unstamped folders"
else
    echo "${p} Data folder does NOT exist"
    if mkdir -vp "${base_folder}"; then
        echo "${p} Created Data Folder --> ${base_folder}"
    else
        echo "${p} Unable to create Data Folder..... exiting"
        exit 2
    fi
fi

# if cp -v "${unstamped_zipfile}" "${unstamped_folder}"
mkdir -vp "${unstamped_folder}"
mkdir -vp "${stamped_folder}"
mkdir -vp "${stamps_folder}"

cp -v "${rstamp_file}" "${stamps_folder}"

unzip -qo "${unstamped_zipfile}" -d "${unstamped_folder}"
# tar -zxf "${unstamped_zipfile}" --strip-components=1 -C "${unstamped_folder}"

# replacement_path="${stamped_folder}"
echo "Path to replace: -->> ${path_to_replace}"
echo "Replacement Path: --> ${stamped_folder}"

echo "${p} Local Installed Python Version is: $(python3 --version)"

python3 -m venv "${python_env_name}"
source "${python_env_name}/bin/activate"
pip install --upgrade pymupdf

# python3 stamp.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${unstamped_zipfile}" "${stamped_folder}" "${path_to_replace}"

python3 glob1.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${unstamped_zipfile}" "${stamped_folder}" "${path_to_replace}" "${stamped_folder_name}"


deactivate

# mkdir -vp "${final_folder}"
# cp -rv "${stamped_folder}" "${final_folder}"

