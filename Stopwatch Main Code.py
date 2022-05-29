# Sound Effects
# Functions that searches the sound and plays it.
import pygame
from pygame import mixer

pygame.mixer.init()

def clear_laps_sound():
    CLEARRR = mixer.Sound('CLEAR.wav')
    CLEARRR.play(0)

def lap_sound():
    LAPSSS = mixer.Sound('LAP.wav')
    LAPSSS.set_volume(0.2)
    LAPSSS.play(0)

def start_default():
    pygame.mixer.music.load('DEFAULT.wav')
    pygame.mixer.music.play(-1)

def start_soundtrack1():
    pygame.mixer.music.load('Ang Wakas.wav')
    pygame.mixer.music.play(-1)

def start_soundtrack2():
    pygame.mixer.music.load('Orange.wav')
    pygame.mixer.music.play(-1)

def start_soundtrack3():
    pygame.mixer.music.load('Royalty Free.wav')
    pygame.mixer.music.play(-1)

def start_soundtrack4():
    pygame.mixer.music.load('Star Blossom.wav')
    pygame.mixer.music.play(-1)

def start_soundtrack5():
    pygame.mixer.music.load('Well Meet Again.wav')
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

# Canvas background
frame = Frame(root)
frame.pack

canvas = Canvas(frame, bg='black', width=350, height=550)
canvas.pack

nightbg = PhotoImage(file='dar.png')
lightbg = PhotoImage(file='lig.png')


lightMode = Label(root, image=lightbg)
lightMode.place(x=0,y=0,relwidth=1,relheight=1)


# Create a menu for changing the sound track.
from tkinter import Menu

my_menu= Menu(root)
root.configure(menu=my_menu)

file_menu = Menu (my_menu, tearoff=0)
my_menu.add_cascade(label="Music", menu= file_menu)

#Button for nightmode and lightmode
button_mode=True

def customize ():
    global button_mode
    global label



    if button_mode:
        button.config(image=noff,bg="#3520BC",activebackground="#3520BC")
        label.config(bg='#4831DF', fg='white', font='Minecraft 40 bold')   
        root.config(bg="#3520BC")
        button_mode=False
        lightMode.config(image=nightbg)
        music_toggle_label.config(bg='#4D36E9',fg='white')
        music_toggle_button.config(bg='#4D36E9')
        action_label.config(bg='#533CFA',fg='white')
        label2.config(bg='#3733B8')
        
    else:
        button.config(image=lion,bg="#2DC3C9",activebackground="#2DC3C9")
        label.config(bg='#91B7AC',font='Minecraft 40 bold')
        root.config(bg="#2DC3C9")
        button_mode= True
        lightMode.config(image=lightbg)
        music_toggle_label.config(bg='#CAAF9C',fg='black')
        music_toggle_button.config(bg='#CAAF9C')
        action_label.config(bg='#F0A896', fg='black')
        label2.config(bg='#5F8D8A')

lion=PhotoImage(file=r'li.png')
noff=PhotoImage(file=r'da.png')

button= Button(root,image=lion,bd=0,bg="#2DC3C9", activebackground="#2DC3C9",command=customize)
button.pack(side=TOP, anchor=NW, )


# Fixing the window size and labels
root.geometry('350x650')
root.resizable(0,0)
label = Tkinter.Label(root, text='00:00:00',bg='#91B7AC', fg='white', font='Minecraft 40 bold')
label.pack(anchor='center', pady=50)


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

music_toggle_label = Label(g,text="Music",bg='#CAAF9C',border=0,font=('bold',11), fg='black')
music_toggle_button = Button(g,image=M_button_on,border=0,command=off, bg='#CAAF9C')
g.pack(anchor='center', pady=5)
music_toggle_label.pack(side='left')
music_toggle_button.pack(side='left')


# Continuation of the labels
action_label = Tkinter.Label(root, text='Press Start to run stopwatch.', bg='#F0A896', fg='black', font='Calibri 12 italic')
action_label.pack(anchor='center', pady=20)
label2 = Tkinter.Label(root, text='LAPS:', bg='#5F8D8A',fg='white', font='Calibri 10 bold')
label2.pack()
f = Tkinter.Frame(root)

# Buttons
clear_laps = Tkinter.Button(f, font='Minecraft 10 bold',text='Clear', bg='#84C355', width=6, state='disabled', command=lambda:[Clear(), clear_laps_sound()])
lap = Tkinter.Button(f, font='Minecraft 10 bold',text='Split', bg='#CCDC4E', width=6, state='disabled', command=lambda:[Lap(), lap_sound()])
start = Tkinter.Button(f, font='Minecraft 10 bold',text='Start', bg='#FEF5E7', width=6, command=lambda:[Start(label), start_default()])
stop = Tkinter.Button(f, font='Minecraft 10 bold',text='Stop', bg='#F1E693', width=6, state='disabled', command=lambda:[Stop(), stop_sound()])
reset = Tkinter.Button(f, font='Minecraft 10 bold',text='Reset', bg='#FFEB53', width=6, state='disabled', command=lambda:[Reset(label), reset_sound()])

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

# Functions for changing soundtrack.
def default():
    start.configure(command=lambda:[Start(label), start_default()])

def soundtrack_1():
    start.configure(command=lambda:[Start(label), start_soundtrack1()])

def soundtrack_2():
    start.configure(command=lambda:[Start(label), start_soundtrack2()])

def soundtrack_3():
    start.configure(command=lambda:[Start(label), start_soundtrack3()])

def soundtrack_4():
    start.configure(command=lambda:[Start(label), start_soundtrack4()])

def soundtrack_5():
    start.configure(command=lambda:[Start(label), start_soundtrack5()])

# Creating code for the contents of the Music menu
file_menu.add_command(label= "Default", command= default)

file_menu.add_command(label= "Soundtrack 1", command= soundtrack_1)

file_menu.add_command(label= "Soundtrack 2", command= soundtrack_2)

file_menu.add_command(label= "Soundtrack 3", command= soundtrack_3)

file_menu.add_command(label= "Soundtrack 4", command= soundtrack_4)

file_menu.add_command(label= "Soundtrack 5", command= soundtrack_5)

#About Us
#About Us
from tkinter import *
root = Tk()
root.minsize(height = 50, width = 100)
root.resizable(0,0)
def tab1():
	pass
    def tab2():
	my_w_tab2=Toplevel(my_w)
	my_w_tab2.geometry("200x200")
	my_w_tab2.title("About Us")
	label=tk.Label(my_w_tab2, textvariable=my_str1)
	label.grid(row=2, column=2,padx=10,pady=30)
	my_str.set("We are a group of 1st Year College students taking up the degree:\n"
        "Bachelor of Science in Electronics and Communications Engineering.\n"
        "Objective: This repository was created for the sole purpose of completing the final project of our Object-oriented Programming course.\n" 
        "We were tasked to create a Python Stopwatch with a GUI using a library of our choice." 
	"Welcome to the Moontong-Underpaid-Devs:\n"
        " Joshua Padayao,\n"
        "Anne Cornelia,\n" 
        "Rizza Claire Mollaneda,\n"
        "Sharry Celines Marcos,\n"
        "John Nicole Losaria\n",
        font = ('Times_New_Roman',10))
       

root.mainloop()
