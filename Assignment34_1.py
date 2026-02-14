import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = folder + "_" + timestamp + ".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()
    return zip_name


def Calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    
    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    
    copied_files = []

    print("Creating the Backup folder for Backup process")

    os.makedirs(Destination, exist_ok = True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok = True)

            #copy the files if its new 
            if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                shutil.copy2(src_path,dest_path)
                copied_files.append(relative)
    
    return copied_files


def MarvellousDataShieldStart(Source = "Data"):
    Border = "-"*50

    BackupName = "MarvellousBackup"

    lobj = open("Logfile","w")
    lobj.write(Border+"\n")
    lobj.write("Backup process started successfully at :"+str(time.ctime())+"\n")
    lobj.write(Border+"\n")

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)
    print("Backup completed successfully")
    lobj.write("Files copied:"+str(len(files))+"\n")
    lobj.write("Zip file name:"+zip_file+"\n")
    lobj.write(Border)


def main():
    
    Border = "-"*50
    print(Border)
    print("-------Marvellous Data Shield system--------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to:")
            print("1 : Text auto backup at givn time")
            print("2 : Backup only new and updated files")
            print("3 : Create and archive of backup periodically")


        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval:The time in minutes for periodic scheduling")
            print("Source Directory:Name of directory to backed up")
            

        else:
            print("Unable to proceed as there is no such option")
            print("Plese use --h or --u to get more commands")

    #python Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval:",sys.argv[1])
        print("Directory name:",sys.argv[2])

        # apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print("Data Shield System started successfully")
        print("Time interval in minutes:",sys.argv[1])
        print("Press Ctrl+C to stop the execution")

        #wait till abort
        while(True):
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as ther is no such option")
        print("Plese use --h or --u to get more commands")

    print(Border)
    print("-----------Thank for using our script-------------")
    print(Border)


if __name__ == "__main__":
    main()