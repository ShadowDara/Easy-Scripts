import tkinter as tk
from tkinter import filedialog

try:
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select the root folder for the server!")

    if not folder_path:
        print("Kein Ordner ausgewählt!")
    else:
        print(f"Ausgewählter Ordner: {folder_path}")

except Exception as e:
    print(f"Fehler: {e}")
