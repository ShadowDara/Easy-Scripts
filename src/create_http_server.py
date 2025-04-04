# script written by Shadowdara

import os
import sys

import http.server
import socketserver

import tkinter as tk
from tkinter import filedialog

import socket

# vars
vdo_print = True

# functions
def do_print(text):
    if vdo_print:
        print(text)

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.bind(('127.0.0.1', port))
        s.close()
        do_print(f"port {port} is usable.")
    except:
        do_print(f"port {port} is busy!")
        return False
    return True

# run on execution
try:
    sys.argv[1]

    if not sys.argv[1].isdigit():
        raise ValueError

    argh_1 = sys.argv[1]

    if sys.argv[1] >= 2:
        argh_1 -= 2

        if check_port(sys.argv[3]):
            do_print(0)
            sys.exit(0)

        else:
            do_print(1)
            sys.exit(1)


    if sys.argv >= 1:
        argh_1 -= 1
        vdo_print = False

except:
    pass

if vdo_print:
    do_print("Terminal Output is set to true!")

try:
    sys.argv[2]
    if sys.argv[2] == '\\':
        os.getcwd()
    else:
        os.chdir(sys.argv[1])

except:
    try:
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory(title="Select the root folder for the server!")
        os.chdir(folder_path)
    except:
        do_print("Could not select folder path!")
        sys.exit(8)

do_print("Simple HTTP Server script by Shadowdara\n")

try:
    sys.argv[3]
    check_port(sys.argv[3])
    PORT = sys.argv[3]

except:
    PORT = 8000
    while True:
        if check_port(PORT):
            break

        elif PORT <= 49150:
            choice = input("Did not found a usable Port, type in a port number [n to close]: ")
            if choice == 'n':
                sys.exit(9)
            else:
                try:
                    if check_port(choice):
                        PORT = choice
                    else:
                        do_print("Port is not usable")
                except:
                    do_print("Could not check the Port")
        PORT += 1

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        do_print("\nhttps://github.com/ShadowDara/Easy-Scripts\nthe source repository with more information and guides\n")
        do_print(f"server runs on http://localhost:{PORT}\n")
        httpd.serve_forever()

except:
    do_print("Server could not started!")
    sys.exit(1)
