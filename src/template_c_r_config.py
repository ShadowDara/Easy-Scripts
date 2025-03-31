# script is written by Shadowdara

import os

config_name = "template.config"

def config_file_content_set():
    global config_file_content
    config_file_content = """# config file templayte by Shadowdara
path = C:\Users\schueler\Desktop
name = Shadowdara
"""

def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", skript_dir)

def create_config_file():
    try:
        with open(config_name, "wt", encoding="uft-8") as config_file:
            config_file.write(config_file_content)
    except:
        print(f"File {config_name} could not be created!")

def check_config_file():
    try:
        with open(config_name, "r", encoding="uft-8") as config_file:
            lines = config_file.readlines()
            return lines
    except:
        create_config_file()
        try:
            with open(config_name, "r", encoding="uft-8") as config_file:
                lines = config_file.readlines()
                return lines
        except:
            print("Could not read the config file!")

# for changing the variables in the config file
def change_config_file():
    lines = check_config_file()
    while True:
        for line in lines:
            x = 1
            if not line.lstrip().startswith("#"):
                print(x + ": " + line, end='')
            x += 1
        if x >= 1: x -= 1
        choice = input("Do you want to change a line? [n for exit]: ")
        if choice == 'n': break
        elif choice in range(0, x):
            before_line = lines[choice].split('=', 1)[0].rstrip()
            after_line = input(f"New Value for {before_line}: ")
            print(f"New Value assignef for {before_line}: {after_line}")
            lines[choice] = before_line + " = " + after_line
        else:
            print("Wrong input")
    try:
        with open(config_name, "wt", encoding="utf-8") as config_file:
            lines.write(lines)
    except:
        print("Missing file writing permission")

# for reading the saved variables
def read_config_file():
    lines = check_config_file
    variables = {}
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            variables[key.strip()] = value.strip()

# run on execution
path()
change_config_file()
