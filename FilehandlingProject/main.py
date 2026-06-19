from pathlib import Path
import os
def readfilesandfolders():
    path = Path("")
    items = list(path.rglob("*")) # recursively find every single file, folder, and 
    # subdirectory within a given directory tree
    for i,items in enumerate(items):
        print(f"{i+1} : {items} ")

def createfile():
    readfilesandfolders()
    try:
        name = input("Enter the file name:")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Enter the text:")
                fs.write(data)
            print("File created successfully.")
        else:
            print("This file already exist.")
    except Exception as err:
        print(f"An error occured as {err}")
    
def readfile():
    readfilesandfolders()
    try:
        name = input("Enter the file name:")
        p = Path(name) #Path working: if name exists then we receive the file path else it will create a path.
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)
            print("File readed successfully.")
        else:
            print("The file does not exist.")
    except Exception as err:
        print(f"An error occured as {err}")
        
def updatefile():
    readfilesandfolders()
    try:
        name = input("Enter the file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
                print("1. File name Edit: ")
                print("2. File content overwrite: ")
                print("3. File content add: ")
                res = int(input("Enter your respone: "))
                if res == 1:
                    name2 = input("Enter the new file name: ")
                    p2 = Path(name2)
                    p.rename(p2)
                if res == 2:
                    with open(p,"w") as fs:
                        data = input("Enter the new content: ")
                        fs.write(data)
                if res == 3:
                    with open(p,"a") as fs:
                        data = input("Add the content: ")
                        fs.write(" "+ data)
        print("File updated successfully.")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    readfilesandfolders()
    try: 
        name = input("Enter the file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removes successfully.")
        else:
            print("File does not exists.")
    except Exception as err:
        print(f"An error occured as {err}")


print("------ File Handling CRUD Operations ------")
print("------ 1: Create a file ------")
print("------ 2: Read a file ------")
print("------ 3: Update a file ------")
print("------ 4: Delete a file ------")

check = int(input("Enter your response: "))

if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()
