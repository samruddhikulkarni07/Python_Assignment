import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

HISTORY_FILE = "HistoryFile"
log_file_path = None
zip_name = None

def make_zip(folder):
    global zip_name

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

            fileextension = ".py"
            if(not file.endswith(fileextension)):
            #copy the files if its new 
                if((not os.path.exists(dest_path)) or (Calculate_hash(src_path) != Calculate_hash(dest_path))):
                    shutil.copy2(src_path,dest_path)
                    copied_files.append(relative)
    
    return copied_files


def MarvellousDataShieldStart(Source = "Data"):
    global log_file_path 
    global HISTORY_FILE

    Border = "-"*50

    BackupName = "MarvellousBackup"

    lobj = open("Logfile","w")
    log_file_path = "LogFile"

    lobj.write(Border+"\n")
    lobj.write("Backup process started successfully at :"+str(time.ctime())+"\n")
    lobj.write(Border+"\n")

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    zip_size = os.path.getsize(zip_file)

    
    hobj = open(HISTORY_FILE,"a")
    hobj.write("Date:"+str(time.ctime())+"\n")
    hobj.write("Number of files copied:"+str(len(files))+"\n")
    hobj.write("zip Size:"+str(zip_size)+"bytes\n")

    print("Backup completed successfully")
    lobj.write("Files copied:"+str(len(files))+"\n")
    lobj.write("Zip file name:"+zip_file+"\n")
    lobj.write(Border)

def Sent_mail(sender,app_password,receiver,subject):
    global log_file_path
    global zip_name


    if log_file_path is None:
        return

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(zip_name)

    with open(log_file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename = os.path.basename(log_file_path),
        )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)
 
    smtp.quit()

    print("Email sent successfully")

def RestoreZip(zip_file,destination):
    if not os.path.exists(zip_file):
        print("Zip file is not exists")

    os.makedirs(destination,exist_ok=True)

    with zipfile.ZipFile(zip_file,'r') as zobj:
        zobj.extractall(destination)

    print("Backup restored successfully to:",destination)

def HistoryTracker():
    global HISTORY_FILE
    
    if not os.path.exists(HISTORY_FILE):
        print("No backup history found")
        return

    else:
        hobj = open(HISTORY_FILE,"r")
        Data = hobj.read()
        print(Data)


    
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
            
        elif(sys.argv[1]=="--history"):
            HistoryTracker()

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

        sender_email = "samruddhikulkarni168@gmail.com"

        app_password = "zmoo bwku ustj imqk"

        receiver_email = "sk5835527@gmail.com"

        subject = "Data shield"

        schedule.every(1).minute.do(Sent_mail,sender_email,app_password,receiver_email,subject)


        print("Data Shield System started successfully")
        print("Time interval in minutes:",sys.argv[1])
        print("Press Ctrl+C to stop the execution")

        #wait till abort
        while(True):
            schedule.run_pending()
            time.sleep(1)

    
    elif(len(sys.argv)==4 and sys.argv[1]=="--restore"):
        zip_file=sys.argv[2]
        destination=sys.argv[3]

        RestoreZip(zip_file,destination)
        return


    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as ther is no such option")
        print("Plese use --h or --u to get more commands")

    print(Border)
    print("-----------Thank for using our script-------------")
    print(Border)


if __name__ == "__main__":
    main()