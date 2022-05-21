# Sound Effects
# Functions that searches the sound and plays it.
import pygame

pygame.mixer.init()

def clear_laps_sound():
    pygame.mixer.music.load('CLEAR.wav')
    pygame.mixer.music.play(0)

def lap_sound():
    pygame.mixer.music.load('LAP.wav')
    pygame.mixer.music.play(0)

def start_default():
    pygame.mixer.music.load('DEFAULT.wav')
    pygame.mixer.music.play(-1)

def stop_sound():
    pygame.mixer.music.load('STOP.wav')
    pygame.mixer.music.play(0)

def reset_sound():
    pygame.mixer.music.load('RESET.wav')
    pygame.mixer.music.play(0)




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
clear_laps = Tkinter.Button(f, text='Clear', width=6, state='disabled', command=lambda:[Clear(), clear_laps_sound()])
lap = Tkinter.Button(f, text='Split', width=6, state='disabled', command=lambda:[Lap(), lap_sound()])
start = Tkinter.Button(f, text='Start', width=6, command=lambda:[Start(label), start_default()])
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=lambda:[Stop(), stop_sound()])
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda:[Reset(label), reset_sound()])

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





# Toggle button for enabling and disabling sound.
# Guide video used: https://youtu.be/nvy56p3P-MM and https://youtu.be/iPqkQS6wFF8

from tkinter import *

g = Tkinter.Frame(root)

M_button_on = PhotoImage(file='Toggle On.png')
M_button_off = PhotoImage(file='Toggle Off.png')


def on():
    music_toggle_button.configure(command=off,image=M_button_on)
    clear_laps.configure(command=lambda:[Clear(), clear_laps_sound()])
    lap.configure(command=lambda:[Lap(), lap_sound()])
    start.configure(command=lambda:[Start(label), start_default()])
    stop.configure(command=lambda:[Stop(), stop_sound()])
    reset.configure(command=lambda:[Reset(label), reset_sound()])

def off():
    music_toggle_button.configure(command=on,image=M_button_off)
    clear_laps.configure(command=Clear)
    lap.configure(command=Lap)
    start.configure(command=lambda: Start(label))
    stop.configure(command=Stop)
    reset.configure(command=lambda: Reset(label))

music_toggle_label = Label(g,text="Music",border=0,font=('bold',11))
music_toggle_button = Button(g,image=M_button_on,border=0,command=off)
g.pack(anchor='center', pady=5)
music_toggle_label.pack(side='left')
music_toggle_button.pack(side='left')



root.mainloop()