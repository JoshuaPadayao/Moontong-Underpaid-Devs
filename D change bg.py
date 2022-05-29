# https://programsolve.com/python-to-create-a-simple-stopwatch-with-source-code/


import tkinter as Tkinter

# canvas
from PIL import Image

# For the listbox
from tkinter import *

# The timer
from datetime import datetime
from tkinter.ttk import Label
from winreg import DeleteKey
counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
			# To manage the intial delay 
            if counter == 0:
                display = '00:00:00'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument 
			# Generally like here we need to call the 
			# function in which it is present repeatedly 
			# Delays by 1000ms=1 seconds and call count again 
            label.after(1000, count)
            counter += 1

	# Triggering the start of the counter. 
    count()

# start function of the stopwatch 
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    lap['state'] = 'normal'
    reset['state'] = 'disabled'
    clear_laps['state'] = 'disabled'
    action_label['text'] = 'Stopwatch running...'

# Stop function of the stopwatch 
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    lap['state'] = 'disabled'
    reset['state'] = 'normal'
    clear_laps['state'] = 'normal'
    running = False
    action_label['text'] = 'Press Start to continue.'

# Lap function of the stopwatch
laps_list = []
def Lap():
    global laps_list
    list_length=len(laps_list)+1
    clear_laps['state'] = 'normal'
    if running:
        laps_list.append("      " + label['text'] + "  " + "Lap" + " " + "#" + str(list_length))
        lap_listbox.delete(0, "end")
        for x in laps_list:
            lap_listbox.insert(0, x)
        action_label['text'] = 'Current time recorded.'
    else:
	    lap['state'] = 'disabled'

# Clear all recorded laps
def Clear():
    laps_list.clear()
    lap_listbox.delete(0, "end")
    clear_laps['state'] = 'disabled'
    action_label['text'] = 'Laps cleared.'

# Reset function of the stopwatch
def Reset(label):
	global counter
	counter = 0
	if not running:
		reset['state'] = 'disabled'
		label['text'] = '00:00:00'
        
	else:
		label['text'] = '00:00:00'

# App title
root = Tkinter.Tk()
root.title("Moontong Stopwatch")
root.iconbitmap('clock-icon.ico')
root.config(bg='white')

# canvas ok.
frame = Frame(root)
frame.pack

canvas = Canvas(frame, bg='black', width=350, height=550)
canvas.pack

nightbg = PhotoImage(file='sydney-australia-skyline-with-op.png')
lightbg = PhotoImage(file='edittt (1) (1).png')


lightMode = Label(root, image=lightbg)
lightMode.place(x=0,y=0,relwidth=1,relheight=1)

#Button for nightmode and lightmode
button_mode=True

def customize ():
    global button_mode
    global label

    if button_mode:
        button.config(image=off,bg="#292929",activebackground="#292929")
        label.config(bg='#292929', fg='white')   
        root.config(bg="#292929")
        action_label.config(bg="#292929", fg='white')
        label2.config(bg="#292929", fg='white')
        button_mode=False
        lightMode.config(image=nightbg)
        #start.config()
    else:
        button.config(image=on,bg="white",activebackground="white")
        label.config(bg='white', fg='black')
        root.config(bg="white")
        action_label.config(bg='white', fg='black')
        label2.config(bg='white', fg='navy')
        button_mode= True
        lightMode.config(image=lightbg)


on=PhotoImage(file='li.png')
canvas.create_image(30, 30, image=on)

off=PhotoImage(file='da.png')
canvas.create_image(30, 30, image=off)

button= Button(root,image=on,bd=0, bg= "#000000", command=customize)
button.pack(side=TOP, anchor=NW)

# Fixing the window size and labels
root.geometry('350x550')
root.resizable(0,0)
label = Tkinter.Label(root, bg='white',text='00:00:00', fg='black', font='Minecraft 40 bold')
label.pack(anchor='center', pady=30)
action_label = Tkinter.Label(root, text='Press Start to run stopwatch.', fg='black', font='Calibri 10 italic', bg='white')
action_label.pack(anchor='center', pady=20)
label2 = Tkinter.Label(root, text='Laps:', fg='black', font='Calibri 10 bold', bg='white')
label2.pack()
f = Tkinter.Frame(root)



# Buttons
clear_laps = Tkinter.Button(f, bg= '#84C355', relief= 'solid',font='Minecraft 10 bold', bd=0, text='Clear', width=6, state='disabled', command=Clear)
lap = Tkinter.Button(f, bg= '#CCDC4E', relief= 'solid',font='Minecraft 10 bold', bd=0, text='Split', width=6, state='disabled', command=Lap)
start = Tkinter.Button(f, bg= '#FEF5E7', relief= 'solid', font='Minecraft 10 bold', bd=0, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, bg= '#F1E693', relief= 'solid', bd=0, font='Minecraft 10 bold', text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, bg= '#FFEB53', relief= 'solid',font='Minecraft 10 bold', bd=0, text='Reset', width=6, state='disabled', command=lambda: Reset(label))

# Create a frame
frame = Frame(root)

# Creating a scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL)

# Listbox for the recorded laps placement
lap_listbox = Listbox(frame, width=20, yscrollcommand=scrollbar.set, selectmode=SINGLE)

# Configure scrollbar
scrollbar.config(command=lap_listbox.yview)

# Packing everything into the screen
scrollbar.pack(side=RIGHT, fill=Y)
frame.pack()
lap_listbox.pack(pady=0)

# Button Placement
f.pack(anchor='center', pady=40)
clear_laps.pack(side='left')
lap.pack(side='left')
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

root.mainloop()