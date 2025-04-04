import os

def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))

#test
import datetime

file = "script.py"  # Ersetze mit deinem Dateinamen
timestamp = os.path.getmtime(file)
last_modified = datetime.datetime.fromtimestamp(timestamp)

print(f"Letzte Änderung: {last_modified}")

path()
