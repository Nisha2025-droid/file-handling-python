from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1} : {items} ")

def readfile():
    try:
        readfileandfolder()
        name = input("which file you want to read")
        p= Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("file read successfully")
        else:
            print("file does not exist")
    except Exception as e:
        print(f"error occurred: {e}")

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete")
        p= Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("file deleted successfully")
        else:
            print("file does not exist")
    except Exception as e:
        print(f"error occurred: {e}")


def udatefile():
    try:
        readfileandfolder()
        name = input("which file you want to update")
        p= Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file")
            print("press 2 for appending data of your file")
            print("press 3 for overwriting data of your file")
            res = int(input("enter your choice"))
            if res==1:
                newname = input("enter new name of your file")
                p2=Path(newname)
                p.rename(p2)
                print("file name changed successfully")
            elif res==2:
                with open(p,'a') as fs:
                    data = input("enter data to append")
                    fs.write(data)
                print("data appended successfully")
            elif res==3:
                with open(p,'w') as fs:
                    data = input("enter data to overwrite")
                    fs.write(data)
                print("data overwritten successfully")
            else:
                print("invalid choice")
    except Exception as e:  
        print(f"error occurred: {e}")



def createfile():
    try:
        readfileandfolder()
        name = input("enter file name")
        p= Path(name)
        if not p.exists() and p.is_file:
            with open(p,'w') as fs:
                data = input("enter data to write")
                fs.write(data)
        else:
            print("file already exists")
        print(f"file created successfully")
    except Exception as e:
     print(f"error occurred: {e}")
    
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 1 for deleting a file")
choice=int(input("enter your choice"))
if choice==1:
    createfile()

if choice==2:
    readfile()

if choice==3:
    udatefile()
if choice==4:
    deletefile()