#!/bin/bash

# unstamped_zipfile=$1

n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)

. ./rs.config
. ./helpers/dirs_create.sh

unstamped_zipfile="${annexure_file}"

base_folder="${data_folder}"

stamps_folder="${base_folder}/${stamps_folder_name}"
stamp_file="${stamps_folder}/${stamp_filename}"

unstamped_folder="${base_folder}/${unstamped_folder_name}"
stamped_folder="${base_folder}/${stamped_folder_name}"

# tmp_unzip_folder="${base_folder}/${tmp_unzip_folder_name}"
images_folder="${base_folder}/${images_folder_name}"

final_folder="${dst_base_folder}/${final_folder_name}"
final_images_folder="${dst_base_folder}/${final_images_folder}"


echo "${p} Checking if file exists"
if [ -f "${unstamped_zipfile}" ]; then
    
    o_user=$(stat -c %U "${unstamped_zipfile}")
    o_group=$(stat -c %G "${unstamped_zipfile}")
    zip_filename=$(basename "${unstamped_zipfile}")
    lowercase_filename=${zip_filename%.*}
    # echo "The Zip file is: ${lowercase_filename}"
    echo "The Zip file is: ${unstamped_zipfile}"

    # path_to_replace="${unstamped_folder}/${lowercase_filename}"
    # echo "${p} File exists and has username as ${o_user} and group as ${o_group}"
else
    echo "${p} File does not exist"
    echo "${p} exiting .. "
    exit 1
fi



echo "${p} Deleting Old Data Folder"
rm -rf "${base_folder}"

echo "${p} Deleting Final Folder"
rm -rf "${final_folder}"

# if [ "$#" -le 0 ]; then
#     echo "${p} File not specified"
#     exit 1
# fi



if [ -d "${base_folder}" ]; then
    echo "${p} Working folder exists. Making internal folder structure"
else
    echo "${p} Working folder does NOT exist"
    if mkdir -vp "${base_folder}"; then
        echo "${p} Created Working Folder --> ${base_folder}"
    else
        echo "${p} Unable to create Working Folder..... exiting"
        exit 2
    fi
fi

# if cp -v "${unstamped_zipfile}" "${unstamped_folder}"


###### optional create folder block ######
# if mkdir -vp "${stamps_folder}"; then
#     echo "${p} created ${stamps_folder}"
# else
#     echo "${p} unable to create ${stamps_folder}"
#     exit 3
# fi


dirs_create "${stamps_folder}" "${unstamped_folder}" "${stamped_folder}" "${images_folder}" "${final_folder}" "${final_images_folder}"

## Copy Stamps
cp -v "${rstamp_file}" "${stamps_folder}"

## Unzip file
unzip -qo "${unstamped_zipfile}" -d "${unstamped_folder}"

STARTTIME=$(date +%s)
### Handing over to Python
echo "${p} Local Installed Python Version is: $(python3 --version)"

python3 -m venv "${python_env_name}"
source "${python_env_name}/bin/activate"
pip install --upgrade pymupdf

# python3 stamp.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${unstamped_zipfile}" "${stamped_folder}" "${path_to_replace}"

python3 stamp4.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${images_folder}"


# python3 stamp5.py "${stamp_file}" "${unstamped_folder}" "${stamped_folder}" "${images_folder}"



# pip3 freeze > requirements.txt
deactivate
### Back to Bash
ENDTIME=$(date +%s)

echo
echo "It took $(($ENDTIME - $STARTTIME)) seconds to complete ..."

### Copy results

echo "Creating Zip ... "
cd "${stamped_folder}"
zip -rq "${final_folder}/stamped_annexures.zip" .
# cp -r "${stamped_folder}" "${final_folder}"
# chown -R "${o_user}:${o_group}" "${final_folder}"
cd ..
chown -R "${o_user}:${o_group}" "${final_folder}/stamped_annexures.zip"

# cp -r "${images_folder}" "${final_images_folder}"
# chown -R "${o_user}:${o_group}" "${final_images_folder}"

# cp -r "${base_folder}" "${final_folder}"
# chown -R "${o_user}:${o_group}" "${final_folder}"


### Cleanup
echo
echo "Performing Cleanup"
rm -rf "${base_folder}"
# rm -rf ""${python_env_name}"


