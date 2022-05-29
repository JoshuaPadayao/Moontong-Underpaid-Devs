from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def new():
 tkinter.messagebox.showinfo('Window Title', 'Well, this is new...')

root = Tk()
root.title("GUI Test Version 2")
root.resizable(False, False)
root.geometry('{}x{}'.format(400, 400))
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Experiment...", command=new)
subMenu.add_command(label="New...", command=new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=new)
toolbar = Frame(root, bg="light blue")
toolbar.pack(side=TOP, fill=X)
class App(object):
    def __init__(self,root):
        self.root = root

        self.txt_frm = Frame(self.root, width=900, height=900)
        self.txt_frm.pack(fill="both", expand=False)
        button1 = Button(self.txt_frm,text="About Us", command = self.AboutUs)
        button1.grid(column=0,row=2, padx=2, pady=2)
        self.label = Label(self.txt_frm,text='')
        self.label.grid(column=0,row=3)
    def AboutUs(self):
        self.label.config(text="Welcome to the Moontong-Underpaid-Devs:"
        " Joshua Padayao,"
        "Anne Cornelia," 
        "Rizza Claire Mollaneda,"
        "Sharry Celines Marcos,"
        "John Nicole Losaria,"
        "We are a group of 1st Year College students taking up the degree: Bachelor of Science in Electronics and Communications Engineering."
        "Objective: This repository was created for the sole purpose of completing the final project of our Object-oriented Programming course. We were tasked to create a Python Stopwatch with a GUI using a library of our choice.") 
status = Label(root, text="Preparing to begin...", bd=1, relief=SUNKEN,     anchor=W) # bd = bordered, relief = ,  appear placed in screen, anchor = w (NESW) needs two other properties
status.pack(side=BOTTOM, fill=X)
app = App(root)
root.mainloop()