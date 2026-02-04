import os 
import sys

def DirectoryScanner(DirName,FileExtension1,FileExtension2):
    Border = "-" * 50

    fobj = open("Samruddhi.Log","w")

    fobj.write(Border+"\n")
    fobj.write("This log file is created by Samruddhi\n")
    fobj.write(f"This is script to change the file{FileExtension1} to {FileExtension2}\n")
    fobj.write(Border+"\n")

    Ret = False
    
    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such a directory")
        return 
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not directory")
        return
     
    for FolderName , SubFolderName , FileName in os.walk(DirName):

        for fName in FileName:
            if fName.endswith(FileExtension1):
                oldpath = os.path.join(FolderName,fName)
                NewName = fName.replace(FileExtension1 , FileExtension2)            # To replace the extensions of the files

                newpath = os.path.join(FolderName,NewName)
                os.rename(oldpath , newpath)                                        # To rename the extensions of the file 
                fobj.write(f"{oldpath} replaced with {newpath}\n")

    fobj.write(Border+"\n")
    fobj.close()

def main():

    Border = "-" * 50
    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

    if(len(sys.argv) != 4):
        print("Invalid Number of Arguments")
        print("Please specify the number of directory")
        return
    
    DirectoryScanner(sys.argv[1], sys.argv[2] , sys.argv[3])

    print(Border)
    print("---------------Directory Automation---------------")
    print(Border)

if __name__ == "__main__":
    main()