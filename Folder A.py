

import shutil
import os

#set where the source of the files are
source = '/Users/junio/OneDrive/Documnets/GitHub/Python-Projects/Folder A.py/

#set the destination path to filderB
destination = '/Users/junio/OneDrive/Documnets/GitHub/Python-Projects/Folder b.py/
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

import os

os.path.exists('./final_data_2020.csv')
