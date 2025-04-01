# script is written by Shadowdara

import os

def path():
    global script_dir
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", script_dir)

# run on execution
path()
while True:
    print("""
Main
    0 to exit
    1 to
    2 to
    3 to
    4 to
    5 to
    6 to
    7 to
    8 to
    9 to
   10 to
""")
    choice = input("Your Choice: ")
    if choice == '0': break
    elif choice == '1': pass
    elif choice == '2': pass
    elif choice == '3': pass
    elif choice == '4': pass
    elif choice == '5': pass
    elif choice == '6': pass
    elif choice == '7': pass
    elif choice == '8': pass
    elif choice == '9': pass
    elif choice == '10': pass
    else:
        input("Wrong input, try again! ...")
