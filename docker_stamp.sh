#!/bin/bash


n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)
script_run_time=$(date +%H-%M)

echo ${todays_date}
echo ${script_run_time}

### Convert to absolute paths for Docker
. /app/docker_stamp.config
. /app/stamp8_helpers/dirs_create.sh
. /app/stamp8_helpers/check_time.sh



unstamped_zipfile="${annexure_file}"

base_folder="${wip_folder}"
# working_stamps_folder="${base_folder}/${working_stamps_folder_name}"
# working_unstamped_folder="${base_folder}/${unstamped_folder_name}"
# working_folder="${base_folder}/${working_folder_name}"
# final_stamped_folder="${base_folder}/${stamped_folder_name}"

dst_folder="${destination_folder}"

# round_stamp_file="${working_stamps_folder}/${round_stamp_file_name}"

env_base="${env_base_path}"
env_path="${env_base}/${python_env_name}"

echo "Version 0.8d-docker"

### Checking in the PY Script
## Checking Input File characteristics
# echo "**** Checking Input File ****"
# if [ -f "${unstamped_zipfile}" ]; then
#     o_user=$(stat -c %U "${unstamped_zipfile}")
#     o_group=$(stat -c %G "${unstamped_zipfile}")
#     zip_filename=$(basename "${unstamped_zipfile}")
#     lowercase_filename=${zip_filename%.*}
#     echo "    The Zip file is: ${unstamped_zipfile}"
# else
#     echo "${p} ERROR: File does not exist"
#     echo "${p} ERROR: exiting .. "
#     exit 1
# fi

### NOT required if binding volume to /wip
## Creating base working folder
# echo
# echo "**** Creating Base Folder ****"
# if [ -d "${base_folder}" ]; then
#     echo "${p} Deleting Old Data Folder and making a new one"
#     rm -rf "${base_folder}"
#     dirs_create "${base_folder}"
# else
#     if mkdir -p "${base_folder}"; then
#         echo "${p} Created Working Folder --> ${base_folder}"
#     else
#         echo "${p} ERROR: Unable to create Working Folder..... exiting"
#         exit 2
#     fi
# fi


log_file_name="${lowercase_filename}__${todays_date}__${script_run_time}.txt"
log_file="${dst_folder}/${log_file_name}"

touch "${log_file}"


### Creating in Stamp8
## Creating internal folder structure
# echo
# echo "**** Creating Internal Folder Structure ****"
# dirs_create "${wip_stamps_folder}" "${wip_unstamped_folder}" "${wip_folder}" "${wip_stamped_folder}"

### Py script will read the file directly
## Copying all Stamps 
# echo
# cp -v "${existing_stamps_folder}/${round_stamp_file_name}" "${working_stamps_folder}/"


### Unzipping in the Python Script
## Unzipping Files
# echo
# echo "${p} Unzipping files"
# unzip -qo "${unstamped_zipfile}" -d "${working_unstamped_folder}"

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

python3 stamp8.py | tee -a "${log_file}"
# python3 stamp8.py "${round_stamp_file}" "${working_unstamped_folder}" "${working_folder}" "${final_stamped_folder}" | tee -a "${log_file}"
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
### Zipping in the Py Script
# echo "${p} Creating Zip ... "
# cd "${final_stamped_folder}"
# zip -rq "${dst_folder}/stamped_annexures-${todays_date}__${script_run_time}.zip" .
# cd ../..
# cp "${log_file}" "${dst_folder}/"
# echo "${p} Copied Zip file to output folder ... "

### Not required for Docker
# chown -R "${o_user}:${o_group}" "${dst_folder}"


### For testing only (Copy contents of working folder)
# cp -r "${base_folder}" "${dst_folder}"
# chown -R "${o_user}:${o_group}" "${dst_folder}"

### Not required for Docker
### Cleanup
# echo
# echo "${p} Performing Cleanup"
# rm -rf "${base_folder}"
# rm -rf "./${env_path}"
# echo "${p} Cleanup Complete"

