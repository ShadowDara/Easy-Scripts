# script written by Shadowdara

import os
import sys
import threading
import time

# functions
def get_input():
    global user_input
    user_input = input("Type in file extension (2 seconds zeit) : ")

def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    
def check_folderpath(path):
    pass

# execution
# print("Folder path:", skript_dir)

try:
    sys.argv[1]
    if sys.argv[1] == '\\':
        path = os.getcwd()
    else:
        path = sys.argv[1]
except:
    try:
        path()
    except:
        print("Could not get the folderpath!")
        sys.exit(1)

try:
    check_folderpath(path)
except:
    pass

try:
    sys.argv[1]
    try:
        extension = sys.argv[2]
    except:
        pass
except:
    user_input = None
    thread = threading.Thread(target=get_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout=2)


if user_input is not None:
    print(f"Du hast eingegeben: {user_input}")
else:
    print("Zeit abgelaufen, es geht weiter!")
