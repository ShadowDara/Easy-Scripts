sub_license_text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LICENSE - HTML</title>
    <link rel="stylesheet" href="https://shadowdara.github.io/assets/css/license.css">
</head>
<body>
<h1>LICENSE</h1>
<p>Here are the LICENSES for the files used.</p>

<hr>

<h2>Name</h2>
<pre>
paste LICENSE
</pre>

<hr>

<h2>End Licenses</h2>

</body>
</html>
"""

import os

# get skript Path
def path():
    global skript_dir
    skript_dir = os.path.dirname(os.path.abspath(__file__))
    print("Folder path:", skript_dir)

def start():
    global directory
    directory = input("")
    if directory == '0':
        pass
    elif directory == '.':
        directory = skript_dir
        continue_setup()
    else:
        continue_setup()

def continue_setup():
    pass

def create():
    # Readme.md
    try:
        with open(directory + "/README.md", "r" "utf-8") as readme:
            readme.close()
    except:
        with open(directory + "/README.md", "r" "utf-8") as readme:
            readme.close()
    # License
    try:
        with open(directory + "/license", "r" "utf-8") as license:
            license.close()
    except:
        with open(directory + "/license", "w" "utf-8") as license:
            license.close()
    # sub license
    try:
        with open(directory + "/sub-license.html", "r" "utf-8") as sub_license:
            sub_license.close()
    except:
        with open(directory + "/sub-license.html", "w" "utf-8") as sub_license:
            sub_license.write(sub_license_text)

if __name__ == '__main__':
    path()
    start()
