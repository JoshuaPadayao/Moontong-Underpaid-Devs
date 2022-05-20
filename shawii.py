
from tkinter import*
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


root = Tk()
root.title("Moontong Stopwatch")

# Fixing the window size.
root.geometry("700x550")
root.resizable(0,0) 
label = Label(root, text='Press Start!', fg='navy', font='San_Francisco 30 bold')
label.pack()
f = Frame(root)
start = Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

#button for nightmode
button_mode=True

def customize ():
    global button_mode

    if button_mode:
        button.config(image=off,bg="#26242f",activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode=False
    else:
        button.config(image=on,bg="white",activebackground="white")
        root.config(bg="white")
        button_mode= True
on=PhotoImage(file='Toggle On.dll')
off=PhotoImage(file='Toggle Off.dll')

button= Button(root,image=on,bd=0,bg="white", activebackground="white",command=customize)
button.pack(side=TOP, anchor=NW)


root.mainloop()
