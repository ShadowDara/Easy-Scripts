# script is written by Shadowdara

import os

config_name = "template.config"

def config_file_content_set():
    global config_file_content
    config_file_content = """# config file templayte by Shadowdara
path: 'C:\Users\schueler\Desktop'
name: Shadowdara
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
            config_lines = config_file.readlines()
            
    except:
        create_config_file()

def change_config_file(lines):
    try:
        with open(config_name, "wt", encoding="utf-8") as config_file:
            pass
    except:
        print("Missing file writing permission")

# run on execution
path()
check_config_file()
