

import tkinter
from tkinter import *
import webbrowser 
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

        #self.varBody = StringVar()
        
        self.lblBody = Label(self.master,text='Type in text here: ', font=("Helvetica", 16), fg='black', bg='gray' )
        self.lblBody.grid(row=0, column=0,padx=(30,0), pady=(30,0))
        
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='gray')
        self.lblDisplay.grid(row=3, column=1,padx=(30,0), pady=(30,0))
       
        self.txtBody = Entry(self.master, font=("Helvetica", 16), fg='black', bg='gray' )
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
        f = open('summersale.html','w')
    
        body = self.txtBody.get()
        
        #get the string from the txtBody Entry widget and assign to variable

        print (body)
        
        message = """<html>
        <head></head>
        <body><p>{}</p></body>
        </html>""".format(body)
        
        
        f.write(message)
        f.close()
        webbrowser.open_new('summersale.html')
       
       
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
        app = Tk()
            
        message = ParentWindow(app)

        message.mainloop()
    
    

   
   
