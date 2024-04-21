#!/usr/bin/env python3

from pathlib import Path


def create_path(dst_file, verbose=False):
    
    print("Creating {dst_file}")
    Path(dst_file).mkdir(parents=True, exist_ok=True)
    if verbose == True:
        print("Created {dst_file}")
    
    return
    

def create_paths_from_list(list, verbose=False):

    print("Creating Paths")

    for file in list:
        create_path(file[1])

    
    return
    