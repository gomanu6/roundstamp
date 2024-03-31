#!/bin/bash

unstamped_zipfile=$1

n=$0
p="[${n}]: "

o_user=""
o_group=""

todays_date=$(date +%F)

. ./rs.config

if [ "$#" -le 0 ]; then
    echo "${p} File not specified"
    exit 1
fi

echo "${p} Checking if file exists"
if [ -f "$1" ]; then
    
    o_user=$(stat -c %U ${unstamped_zipfile})
    o_group=$(stat -c %G ${unstamped_zipfile})

    echo "${p} File exists and has username as ${o_user} and group as ${o_group}"
else
    echo "${p} File does not exist"
    echo "${p} exiting .. "
    exit 1
fi

if [ -d "${data_folder}" ]; then
    echo "${p} Data folder exists. Making Stamped and Unstamped folders"
else
    echo "${p} Data folder does NOT exist"
    if mkdir -vp "${data_folder}"; then
        echo "${p} Created Data Folder --> ${data_folder}"
    else
        echo "${p} Unable to create Data Folder..... exiting"
        exit 2
    fi
fi

# if cp -v "${unstamped_zipfile}" "${unstamped_folder}"
mkdir -vp "${unstamped_folder}"
mkdir -vp "${stamped_folder}"

unzip "${unstamped_zipfile}" -d "${unstamped_folder}"




    


