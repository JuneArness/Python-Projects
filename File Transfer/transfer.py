

import shutil
import os

#set where the source of the files are
source = './folder_a.py/'

#set the destination path to filderB
destination = '/folder_b.py/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)

import os

os.path.exists('./text-1.txt/')
