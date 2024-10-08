#!/bin/bash


n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)
script_run_time=$(date +%H-%M)

### Convert to absolute paths for Docker
. ./rs8.config
. ./stamp8_helpers/dirs_create.sh
. ./stamp8_helpers/check_time.sh



unstamped_zipfile="${annexure_file}"
base_folder="${data_folder}"

working_stamps_folder="${base_folder}/${working_stamps_folder_name}"
working_unstamped_folder="${base_folder}/${unstamped_folder_name}"
working_folder="${base_folder}/${working_folder_name}"
final_stamped_folder="${base_folder}/${stamped_folder_name}"

dst_folder="${destination_folder}"

round_stamp_file="${working_stamps_folder}/${round_stamp_file_name}"

env_base="${env_base_path}"
env_path="${env_base}/${python_env_name}"

echo "Version 0.8b"

## Checking Input File characteristics
echo "**** Checking Input File ****"
if [ -f "${unstamped_zipfile}" ]; then
    o_user=$(stat -c %U "${unstamped_zipfile}")
    o_group=$(stat -c %G "${unstamped_zipfile}")
    zip_filename=$(basename "${unstamped_zipfile}")
    lowercase_filename=${zip_filename%.*}
    echo "    The Zip file is: ${unstamped_zipfile}"
else
    echo "${p} ERROR: File does not exist"
    echo "${p} ERROR: exiting .. "
    exit 1
fi

## Creating base working folder
echo
echo "**** Creating Base Folder ****"
if [ -d "${base_folder}" ]; then
    echo "${p} Deleting Old Data Folder and making a new one"
    rm -rf "${base_folder}"
    dirs_create "${base_folder}"
else
    if mkdir -p "${base_folder}"; then
        echo "${p} Created Working Folder --> ${base_folder}"
    else
        echo "${p} ERROR: Unable to create Working Folder..... exiting"
        exit 2
    fi
fi


log_file_name="${zip_filename}__${todays_date}__${script_run_time}.txt"
log_file="${base_folder}/${log_file_name}"

touch "${log_file}"


## Creating internal folder structure
echo
echo "**** Creating Internal Folder Structure ****"
dirs_create "${working_stamps_folder}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}"


## Copying all Stamps
echo
cp -v "${existing_stamps_folder}/${round_stamp_file_name}" "${working_stamps_folder}/"


## Unzipping Files
echo
echo "${p} Unzipping files"
unzip -qo "${unstamped_zipfile}" -d "${working_unstamped_folder}"

STARTTIME=$(date +%s)


### Handing over to Python
echo
echo "${p} Local Installed Python Version is: $(python3 --version)"
echo

echo "---> Handing over to Python"
python3 -m venv "${env_path}"
source "${env_path}/bin/activate"
pip install --upgrade "${python_modules}"

echo

python3 stamp8.py "${round_stamp_file}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}" | tee -a "${log_file}"
# python3 stamp6.py "${round_stamp_file}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}"

# pip3 freeze > requirements.txt
deactivate


### Back to Bash

ENDTIME=$(date +%s)
echo

check_time $STARTTIME $ENDTIME

# TOTALTIME=$(($ENDTIME - $STARTTIME))


# REPORT_UOM="seconds"
# REPORT_TIME="${TOTALTIME}"
# echo "It took $(($ENDTIME - $STAR   TTIME)) seconds to complete ..."

# if [[ $TOTALTIME ge 60 ]]; then
#     REPORT_TIME=$(($TOTALTIME / 60))
#     REPORT_UOM="minutes"
# fi
# echo "It took ${REPORT_TIME} ${REPORT_UOM} to complete ..."

# echo "It took ${TOTALTIME} ${REPORT_UOM} to complete ..."
echo


### Not required for Docker
### Deleting Old Destination Folder
# if [ -d "${dst_folder}" ]; then
#     echo "${p} deleting previous destination folder"
#     rm -rf "${dst_folder}"
# fi


### Not required for Docker
### Creating Destination Folder
# dirs_create "${dst_folder}"


### Copy results
echo "${p} Creating Zip ... "
cd "${final_stamped_folder}"
zip -rq "${dst_folder}/ASC-10499-uma-stamped_${todays_date}__${script_run_time}.zip" .
cd ../..
cp "${log_file}" "${dst_folder}/"

### Not required for Docker
chown -R "${o_user}:${o_group}" "${dst_folder}"


### For testing only (Copy wcontents of working folder)
# cp -r "${base_folder}" "${dst_folder}"
# chown -R "${o_user}:${o_group}" "${dst_folder}"

### Not required for Docker
### Cleanup
echo
echo "${p} Performing Cleanup"
rm -rf "${base_folder}"
rm -rf "./${env_path}"
echo "${p} Cleanup Complete"

