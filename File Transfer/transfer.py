

import shutil
import os
from tkinter import filedialog 

import tkinter as tk
from tkinter import *


# If we look over the assignment guidelines first we will need two buttons. One for selecting the source folder and then one for selecting the destination folder.

# We will also need two entry fields for the folder path strings to be stored into after the user selects the source and destination folders.

# Lastly, we need another button that will call the function to move the files when clicked.

# This covers all the guidelines needed for this assignment.

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self, master)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('')
        self.master.config(bg='lightgray')

        self.varSource = StringVar()
        self.varDestination = StringVar()

        

        self.lblSource = Label(self.master,text='Source', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblSource.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        
        self.lblDestination = Label(self.master,text='Destination', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblDestination.grid(row=1, column=0,padx=(30,0), pady=(30,0))


        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
       
        self.txtSource = Entry(self.master,text=self.varSource, font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.txtSource.grid(row=0, column=1,padx=(30,0), pady=(30,0))

        self.txtDestination = Entry(self.master,text=self.varDestination, font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.txtDestination.grid(row=1, column=1,padx=(30,0), pady=(30,0))

        self.txtMove = Entry(self.master,text=self.varDestination, font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.txtMove.grid(row=1, column=1,padx=(30,0), pady=(30,0))


        self.btnSource = Button(self.master, text="Source", width=10, height=2, command = self.source)
        self.btnSource.grid(row=3, column=1,padx=(0,10), pady=(30,0), sticky=NE)
                
        

        self.btnDestination = Button(self.master, text="Destination", width=10, height=2, command = self.destination)
        self.btnDestination.grid(row=3, column=2,padx=(0,10), pady=(30,0), sticky=NE)

        

        

        self.btnMove = Button(self.master, text="Move", width=10, height=2, command = self.move)
        self.btnMove.grid(row=3, column=0,padx=(0,10), pady=(30,0), sticky=NE)


        # Here I am creating 3 buttons. for source, desitination, and to move the files:
        # the source button should allow user to chose where the folder is stored at to start;
        # the destination button should allow user to chose where they would like the folder to be stored at to end;
        # the move button should allow user to initiate the actual transfer from source to destination.
        
    def source(self):
        src = filedialog.askdirectory()
        self.txtSource.insert(END, src)
        
    def destination(self):
        dest = filedialog.askdirectory()
        self.txtDestination.insert(END, dest)

    def move(self):
        source = self.txtSource.get()
        destination = self.txtDestination.get()
        

        #set where the source of the folder are
        #source = 'C:/Users/junio/OneDrive/Documents/GitHub/Python-Projects/File Transfer/SRC'

        #set the destination path to folderB
        #destination = 'C:/Users/junio/OneDrive/Documents/GitHub/Python-Projects/File Transfer/DEST'
        files = os.listdir(source) 

        for i in files:
            #we are saying move the files represented by 'i' to their new destination
            shutil.move(source+"/"+i, destination)
        # Here is where the text file is called:
        

       




if __name__ == "__main__":
        app = Tk()
            
        chose = ParentWindow(app)

        chose.mainloop()
    

