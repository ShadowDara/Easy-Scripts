import os
import sys

# Restart for Errors
def restart_program():
    input("Restarting Programm (Press Enter) ... \n")
    os.execv(sys.executable, ['python'] + sys.argv)

# get skript Path
def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", skript_dir)

def start():
    pass

if __name__ == '__main__':
    path()
    start()
