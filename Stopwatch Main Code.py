# https://programsolve.com/python-to-create-a-simple-stopwatch-with-source-code/


import tkinter as Tkinter

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

# Fixing the window size and labels
root.geometry('700x550')
root.resizable(0,0)
label = Tkinter.Label(root, text='00:00:00', fg='navy', font='Calibri 40 bold')
label.pack(anchor='center', pady=50)
action_label = Tkinter.Label(root, text='Press Start to run stopwatch.', fg='black', font='Calibri 10 italic')
action_label.pack(anchor='center', pady=20)
label2 = Tkinter.Label(root, text='Laps:', fg='navy', font='Calibri 10 bold')
label2.pack()
f = Tkinter.Frame(root)

# Buttons
clear_laps = Tkinter.Button(f, text='Clear', width=6, state='disabled', command=Clear)
lap = Tkinter.Button(f, text='Split', width=6, state='disabled', command=Lap)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))

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