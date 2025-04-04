# script written by Shadowdara

import os
import sys

import tkinter as tk
from tkinter import filedialog

# vars
show_noacces = False
direct_folder = False
do_wait = True
vdo_print = True

# functions
def do_print(text):
    if vdo_print:
        print(text)

def search_subfolder(folder_path):
    size = 0
    if os.path.isdir(folder_path):
        filename = os.path.basename(folder_path)
        do_print(f"{filename}/ : {list_files_and_dirs(folder_path, size)} Bytes")

    else:
        try:
            size = os.path.getsize(folder_path)
            filename = os.path.basename(folder_path)
            do_print(f"{filename} - {size} Bytes")
        except:
            pass

def list_files_and_dirs(directory, size):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:

                if entry.is_file():
                    size += os.path.getsize(entry.path)

                elif entry.is_dir():
                    size += list_files_and_dirs(entry.path, size)

    except PermissionError:
        if show_noacces:
            do_print(f"No Access: {directory}")

    return size

# run on execution
try:
    sys.argv[1]

    if not sys.argv[1].isdigit():
        raise ValueError

    argh_1 = sys.argv[1]

    if argh_1 >= 8:
        argh_1 -= 8
        show_noacces = True

    if sys.argv >= 4:
        argh_1 -= 4
        direct_folder = True

    if sys.argv >= 2:
        argh_1 -= 2
        do_wait = False

    if sys.argv >= 1:
        argh_1 -= 1
        vdo_print = False

except:
    pass

do_print("Simple folder size index script by Shadowdara\n\nTerminal Output is set to true!\n\nhttps://github.com/ShadowDara/Easy-Scripts\nthe source repository with more information and guides\n")

try:
    sys.argv[2]
    if not sys.argv[2] == '$$0':
        if sys.argv[2] == '\\':
            folder_path = os.getcwd()
        else:
            if os.path.isdir(sys.argv[2]):
                folder_path = os.chdir(sys.argv[2])
            else:
                do_print("Folder path from argh does not work!")
    else:
        raise ValueError

except:
    try:
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(title="Select the root folder for the server!")

    except:
        print("Could not select folder path!")
        sys.exit(8)

if not direct_folder:
    #try:
        for d in os.listdir(folder_path):
            new_folder_path = folder_path
            new_folder_path = os.path.join(folder_path, d)
            print(new_folder_path)
            search_subfolder(folder_path)

    #except:
        #do_print("Could not serach through the folders!")
        #sys.exit(1)

else:
    search_subfolder(folder_path)

if do_wait:
    input("Press Enter to exit")

sys.exit(0)
