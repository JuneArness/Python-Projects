

import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __int__ (self, master):
        Frame.__int__ (self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='light gray')

        varFName = StringVar()
        varLName = StringVar()
        varFName.set('Bob')
        varLName.set('Smith')

        print(self.varFName.get())
        print(self.varLName.get())
        
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lighblue')
        self.txtFName.pack()

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lighblue')
        self.txtLName.pack()



if __name__=="__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    
