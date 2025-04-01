# script written by Shadowdara

import os
import sys

import http.server
import socketserver

import tkinter as tk
from tkinter import filedialog

import socket

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.bind(('127.0.0.1', port))
        s.close()
        print(f"port {port} is usable.")
    except socket.error as e:
        print(f"port {port} is busy!")
        return False
    return True

try:
    sys.argv[3]
    if sys.argv[3] == '2':
        if check_port(sys.argv[2]) == True:
            sys.exit(0)
        else:
            sys.exit(1)
except:
    pass

try:
    sys.argv[1]
    if sys.argv[1] == '\\':
        os.getcwd()
    else:
        os.chdir(sys.argv[1])

except:
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select the root folder for the server!")
    os.chdir(folder_path)

print("Simple HTTP Server script by Shadowdara\n")

try:
    sys.argv[2]
    check_port(sys.argv[2])
    PORT = sys.argv[2]

except:
    PORT = 8000
    while True:
        if check_port(PORT) == True:
            break

        elif PORT <= 49150:
            choice = input("Did not found a usable Port, continue search? [y, n]: ")
            if choice == 'y':
                PORT = 1024
            else:
                sys.exit(9)
        else:
            PORT += 1

Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\nhttps://github.com/ShadowDara/Easy-Scripts\nthe source repository with more information and guides\n")
        print(f"server runs on http://localhost:{PORT}\n")
        httpd.serve_forever()
except:
    print("Server could not started!")
    sys.exit(1)
