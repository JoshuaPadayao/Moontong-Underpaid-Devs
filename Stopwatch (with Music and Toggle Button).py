# Sound Effects
# Functions that searches the sound and plays it.
import pygame

pygame.mixer.init()

def start_default():
    pygame.mixer.music.load(r'C:\Users\TERESITA M. CORNELIA\Downloads\Ballerina.wav')
    pygame.mixer.music.play(-1)

def stop_sound():
    pygame.mixer.music.load(r'C:\Users\TERESITA M. CORNELIA\Downloads\STOP.wav')
    pygame.mixer.music.play(0)

def reset_sound():
    pygame.mixer.music.load(r'C:\Users\TERESITA M. CORNELIA\Downloads\UWU.wav')
    pygame.mixer.music.play(0)



# https://programsolve.com/python-to-create-a-simple-stopwatch-with-source-code/

import tkinter as Tkinter
from datetime import datetime
counter = 0
running = False

def counter_label(label):
    def count():
        if running:
            global counter
			# To manage the intial delay. 
            if counter == 0:
                display = '00:00:00'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
	
            label['text'] = display
	
			# label.after(arg1, arg2) delays by 
			# first argument given in milliseconds 
			# and then calls the function given as second argument. 
			# Generally like here we need to call the 
			# function in which it is present repeatedly. 
			# Delays by 1000ms=1 seconds and call count again. 
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
    reset['state'] = 'normal'
	

# Stop function of the stopwatch 
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False
	

# Reset function of the stopwatch 
def Reset(label):
	global counter
	counter = 0
	# If reset is pressed after pressing stop. 
	if not running:
		reset['state'] = 'disabled'
		label['text'] = '00:00:00'
	# If reset is pressed while the stopwatch is running. 
	else:
		label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Moontong Stopwatch")

# Fixing the window size.
root.minsize(width=700, height=550)
root.maxsize(width=700, height=550)
label = Tkinter.Label(root, text='Press Start!', fg='navy', font='San_Francisco 30 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:[Start(label), start_default()])
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=lambda:[Stop(), stop_sound()])
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda:[Reset(label), reset_sound()])
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')



# Toggle button for enabling and disabling sound.
# Guide video used: https://youtu.be/nvy56p3P-MM and https://youtu.be/iPqkQS6wFF8

from tkinter import *

g = Tkinter.Frame(root)

M_button_on = PhotoImage(file=r'C:\Users\TERESITA M. CORNELIA\Downloads\Toggle On.png')
M_button_off = PhotoImage(file=r'C:\Users\TERESITA M. CORNELIA\Downloads\Toggle Off.png')


def on():
    music_toggle_button.configure(command=off,image=M_button_on)
    start.configure(command=lambda:[Start(label), start_default()])
    stop.configure(command=lambda:[Stop(), stop_sound()])
    reset.configure(command=lambda:[Reset(label), reset_sound()])

def off():
    music_toggle_button.configure(command=on,image=M_button_off)
    start.configure(command=lambda: Start(label))
    stop.configure(command=Stop)
    reset.configure(command=lambda: Reset(label))

music_toggle_label = Label(g,text="Music",border=0,font=('bold',11))
music_toggle_button = Button(g,image=M_button_on,border=0,command=off)
g.pack(anchor='center', pady=5)
music_toggle_label.pack(side='left')
music_toggle_button.pack(side='left')


root.mainloop()