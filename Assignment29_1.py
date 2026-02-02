import os

def main():
    FileName = input("Enter name of file:")

    Result = os.path.exists(FileName)

    if(Result == True):
        print("File exist in current directory")
    else:
        print("File not exist in current directory") 

if __name__ == "__main__":
    main()