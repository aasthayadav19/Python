import os
from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Enter your file name -")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("what you want to write in this file -")
                fs.write(data)

            print("file created successfully")
        else:
            print("file already exists")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:

        readfileandfolder()
        name = input("which file you want to read -")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)

            print("Readed successfully")
        else:
            print("file does not exists")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("which file you want to update -")
        p = Path(name)

        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for overwriting content of your file")
            print("press 3 for appending content of your file")

            res = int(input("Tell your response -"))

            if res == 1:
                name2 = input("Enter your new file name -")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, "w") as fs:
                    data = input("what you want to write in this file -")
                    fs.write(data)

            if res == 3:
                with open(p, "a") as fs:
                    data = input("what you want to append in this file -")
                    fs.write(" " + data)

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete -")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("file deleted successfully")
        else:
            print("file does not exists")

    except Exception as err:
        print(f"An error occured as {err}")

   
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating  a file")
print("press 4 for deleting a file")

check = int(input("Tell your response: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()    

if check == 4:
     deletefile()    