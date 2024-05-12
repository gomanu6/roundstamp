#!/bin/bash


n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)

. ./rs5.config
. ./helpers/dirs_create.sh

unstamped_zipfile="${annexure_file}"
base_folder="${data_folder}"

working_stamps_folder="${base_folder}/${working_stamps_folder_name}"
working_unstamped_folder="${base_folder}/${unstamped_folder_name}"
working_folder="${base_folder}/${working_folder_name}"
final_stamped_folder="${base_folder}/${stamped_folder_name}"

dst_folder="${destination_folder}"

round_stamp_file="${working_stamps_folder}/${round_stamp_file_name}"

## Checking Input File characteristics
echo "${p} Checking Input File"
if [ -f "${unstamped_zipfile}" ]; then
    o_user=$(stat -c %U "${unstamped_zipfile}")
    o_group=$(stat -c %G "${unstamped_zipfile}")
    zip_filename=$(basename "${unstamped_zipfile}")
    lowercase_filename=${zip_filename%.*}
    echo "The Zip file is: ${unstamped_zipfile}"
else
    echo "${p} File does not exist"
    echo "${p} exiting .. "
    exit 1
fi

## Creating base working folder
if [ -d "${base_folder}" ]; then
    echo "${p} Deleting Old Data Folder and making a new one"
    rm -rf "${base_folder}"
    if mkdir -vp "${base_folder}"; then
        echo "${p} Created Working Folder --> ${base_folder}"
    else
        echo "${p} Unable to create Working Folder..... exiting"
        exit 2
    fi
fi

## Creating internal folder structure
dirs_create "${working_stamps_folder}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}"


## Copying all Stamps
cp -v "${existing_stamps_folder}/${round_stamp_file_name}" "${working_stamps_folder}/"

## Unzipping Files
echo "${p} Unzipping files"
unzip -qo "${unstamped_zipfile}" -d "${working_unstamped_folder}"

STARTTIME=$(date +%s)


### Handing over to Python
echo "${p} Local Installed Python Version is: $(python3 --version)"

python3 -m venv "${python_env_name}"
source "${python_env_name}/bin/activate"
pip install --upgrade "${python_modules}"

python3 stamp5.py "${round_stamp_file}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}"

# pip3 freeze > requirements.txt
deactivate


### Back to Bash

ENDTIME=$(date +%s)
echo
echo "It took $(($ENDTIME - $STARTTIME)) seconds to complete ..."


### Copy results
# echo "Creating Zip ... "
# cd "${final_stamped_folder}"
# zip -rq "${dst_folder}/stamped_annexures.zip" .
# cd ..


if [ -d "${dst_folder}" ]; then
    echo "${p} deleting previous destination folder"
    rm -rf "${dst_folder}"
fi

dirs_create "${dst_folder}"
cp -r "${base_folder}" "${dst_folder}"
chown -R "${o_user}:${o_group}" "${dst_folder}"

### Cleanup
echo
echo "Performing Cleanup"
rm -rf "${base_folder}"
# rm -rf "${python_env_name}"
echo "${p} Cleanup Complete"
