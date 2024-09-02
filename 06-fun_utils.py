import os
import datetime

check_ram_win_command = 'systeminfo | findstr /C:"Total Physical Memory"'
def check_ram():
    print(os.system(check_ram_win_command))

def show_date():
    return datetime.datetime.today()

check_ram()
date=show_date()
print("Today date is ",date)