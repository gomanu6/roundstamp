#!/bin/bash



dirs_create() {

    
    local x="[dir_create]: "


    for folder in "$@"
    do
    
        if [ -n "${folder}" ]; then

            if [ ! -d "${folder}" ]; then
                # echo "${x} ${folder}  doesn't exist, Creating it"
                echo

                if mkdir -p "${folder}" ; then
                    echo "${x} Created Folder ${folder}"
                else
                    echo "${x} Unable to Create ${folder}"
                fi
            else
                echo "${x} ${folder} already exists"
            fi
        else
            echo "${x} Please enter a valid Folder name"
        fi
    done

}
