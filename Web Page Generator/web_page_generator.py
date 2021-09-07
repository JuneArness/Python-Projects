

import tkinter
from tkinter import *



    # write-html.py

f = open('summersale.html','w')

message = """<html>
<head></head>
<body><p>Stay tuned for our amazing summer sale!</p></body>
</html>"""

f.write(message)
f.close()




class ParentWindow(Frame):
    def __int__ (self, master):
        Frame.__int__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Summer Sale!')
        self.master.config(bg='lightblue')

        self.varBody = StringVar()
        
        self.lblBody = Label(self.master,text='Type in text here: ', font=("Helvetica", 16), fg='black', bg='lightgray' )
        self.lblBody.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
       
        self.txtBody = Entry(self.master,text=self.varBody, font=("Helvetica", 16), fg='black', bg='lighgray' )
        self.txtBody.grid(row=0, column=1,padx=(30,0), pady=(30,0))

       

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command = self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command = self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)
        
    def submit(self):
        fn = self.varBody.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()


