import sys
import shutil
import os

def DirectoryScanner(DirName1,DirName2):
    Border = "-"*50

    dobj = os.mkdir(DirName2)
    fobj = open("Samarth.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is the log file created by samruddhi\n")
    fobj.write(f"This is the script for copying files from {DirName1} into {DirName2}\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName1)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName1)
    if(Ret == False):
        print("This is not a directory")
        return

    for FolderName, SubFolderName, FileName in os.walk(DirName1):
        for fname in FileName:
    
            old_path = os.path.join(FolderName,fname)

            new_path = os.path.join(DirName2,fname)

            shutil.copy(old_path,new_path)

            fobj.write(f"{fname} copied from {DirName1} into {DirName2}\n")

    
    fobj.write(Border+"\n")

    fobj.close()



def main():
    Border = "-"*50

    print(Border+"\n")
    print("-----------------Directory Automation----------------\n")
    print(Border+"\n")

    if(len(sys.argv) != 3):
        print("Invalid number of arguments")
        return
    
    DirectoryScanner(sys.argv[1],sys.argv[2])


    print(Border+"\n")
    print("-----------------Directory Automation----------------\n")
    print(Border+"\n")

if __name__ == "__main__":
    main()