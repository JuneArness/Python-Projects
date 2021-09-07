

import shutil
import os

#set where the source of the folder are
source = 'C:/Users/junio/OneDrive/Documents/GitHub/Python-Projects/File Transfer/SRC'

#set the destination path to folderB
destination = 'C:/Users/junio/OneDrive/Documents/GitHub/Python-Projects/File Transfer/DEST'
files = os.listdir(source) 

for i in files:
    #we are saying move the files represented by 'i' to their new destination
    shutil.move(source+"/"+i, destination)

import os

os.path.exists('./text-1.txt/')
