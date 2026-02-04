import sys
import os

def DirectoryScanner(DirName,Fileextension):
    Border = "-"*50
    fobj = open("Assignment.log","w")

    fobj.write(Border+"\n")
    fobj.write("This is a log file created by Samruddhi\n")
    fobj.write(f"This is the Script for finding file with{Fileextension} \n")
    fobj.write(Border+"\n")

    Ret = False 

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It s not a directory")
        return


    for FolderName,SubFolder,FileName in os.walk(DirName):
        
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            if(fname.endswith(Fileextension)):
                fobj.write(fname+"\n")
                

    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("----------------Directory Automation--------------")
    print(Border)

    if(len(sys.argv)!=3):
        print("Invalid numer of arguments")
        print("Please specify the name of directory")
        return

    DirectoryScanner(sys.argv[1],sys.argv[2])

    print(Border)
    print("----------------Directory Automation--------------")
    print(Border)

if __name__ == "__main__":
    main()