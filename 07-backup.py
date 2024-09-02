import shutil
import os
import datetime

def backupfile(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}")
    shutil.make_archive(backup_file_name,'gztar',source)
    

source = r"E:\daws-78s\repos\learn-jenkins"
destination = r"E:\daws-78s\repos\learn-python\backups"
backupfile(source,destination)