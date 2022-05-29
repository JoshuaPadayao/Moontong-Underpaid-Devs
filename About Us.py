#About Us
from tkinter import *
root = Tk()
root.minsize(height = 50, width = 900)
root.resizable(0,0)
def tab1():
    def tab2():
        label1.destroy()
        button1.destroy()
        label2 = Label(root, text = "We are a group of 1st Year College students taking up the degree:\n"
        "Bachelor of Science in Electronics and Communications Engineering.\n"
        "Objective: This repository was created for the sole purpose of completing the final project of our Object-oriented Programming course.\n" 
        "We were tasked to create a Python Stopwatch with a GUI using a library of our choice.",
        font = ('Times_New_Roman',15))
        label2.pack()
        def back():
            label2.destroy()
            button2.destroy()
            tab1()
        button2 = Button(root, text = 'Back', font = ('Times_New_Roman', 15), command = back)
        button2.pack(side = BOTTOM)
    label1 = Label(root, text = "Welcome to the Moontong-Underpaid-Devs:\n"
        " Joshua Padayao,\n"
        "Anne Cornelia,\n" 
        "Rizza Claire Mollaneda,\n"
        "Sharry Celines Marcos,\n"
        "John Nicole Losaria\n", font = ('Times_New_Roman', 15))
    label1.pack()
    button1 = Button(root, text = 'Next', font = ('Times_New_Roman', 15), command = tab2)
    button1.pack(side = BOTTOM)
button = Button(root, text = 'About Us', font = ('Times_New_Roman', 15), command = tab1)
button.pack(side = BOTTOM)

root.mainloop()
