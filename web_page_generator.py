

import tkinter
from tkinter import *
#WHEN THE PROGRAM RUNS WHAT SHOULD HAPPEN?
#STEP 1: GUI SHOULD DISPLAY WITH ENTRY AND BUTTON WIDGET
#STEP 2: USER ENTERS INPUT TO ENTRY WIDGET
#STEP 3: SUBMIT BUTTON IS PRESSED
#STEP 4: PROGRAM WRITES HTML WITH BODY EQUAL TO USER INPUT AND OPENS THE WEBPAGE IN BROWSER
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)
        
        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Summer Sale!')
        self.master.config(bg='gray')

        self.varBody = StringVar()
        
        self.lblBody = Label(self.master,text='Type in text here: ', font=("Helvetica", 16), fg='black', bg='gray' )
        self.lblBody.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='gray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
       
        self.txtBody = Entry(self.master,text=self.varBody, font=("Helvetica", 16), fg='black', bg='gray' )
        self.txtBody.grid(row=0, column=1,padx=(30,0), pady=(30,0))

       

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command = self.submit)
        self.btnSubmit.grid(row=2, column=1,padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command = self.cancel)
        self.btnCancel.grid(row=2, column=1,padx=(0,90), pady=(30,0), sticky=NE)
        
def submit(self):
    #STEP WHAT SHOULD HAPPEN WHEN  SUBMIT IS CALLED
    #STEP 1: function self.varBody is called
    #STEP 2: HTML code is writen
    #STEP 3: HTML page is called
    fn = self.varBody.get()
    
    f = open('summersale.html','w')

    message = """<html>
    <head></head>
    <body><p>Stay tuned for our amazing summer sale!</p></body>
    </html>"""
    
    f.write(message)
    f.close()
    self.lblDisplay.config(text='Hello {} {}!'.format(body))

def cancel(self):
    self.master.destroy()


if __name__ == "__main__":
    app = Tk()
    
    message = ParentWindow(app)

    message.mainloop()
    
    

   
   
