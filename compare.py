#Code source: https://youtu.be/_9tzla_DY9M

#Step 1: Importing the modules. 2:40
from re import I
from tkinter import *
import time
from turtle import width

#Step 2: Creating a screen. 3:13
root = Tk()
root.configure(background=("black"))
root.title("Stopwatch")
root.geometry("980x480")

#Step 3: Creating important variables. 4:49
time_elapsed1=0
time_elapsed2=0
time_elapsed3=0
time1=0
time2=0
i = 0
j = 0

#Step 4: Creating Functions. 6:17
#Function
def create_label(text,_x,_y):
    label=Label(root,text=text,fg="white",bg="black",font=("default",10,"bold"))
    label.place(x=_x,y=_y,width=100,height=45)

def start():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=20,y=300,width=300,height=100)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else:
            time_elapsed1=0
            time_elapsed2+=1
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
            else:
                time_elapsed2=0
                time_elapsed3+=1
                if time_elapsed3>=24:
                    time_elapsed1=0
                    time_elapsed2=0
                    time_elapsed3=0
                else:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(1000,start)

def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job=None
    stop_button.place_forget()
    resume_button.place(x=20,y=300,width=300,height=100)

def resume():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=20,y=300,width=300,height=100)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else:
            time_elapsed1=0
            time_elapsed2+=1
            if time_elapsed2<59:
                time_elapsed2+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
            else:
                time_elapsed2=0
                time_elapsed3+=1
                if time_elapsed3>=24:
                    time_elapsed1=0
                    time_elapsed2=0
                    time_elapsed3=0
                else:
                    time_elapsed3+=1
                    clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(1000,start)

def clear():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,label, i, j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="00:00:00")
    time_elapsed1=0
    time_elapsed2=0
    time_elapsed3=0
    time_1=0
    time_2=0
    i = 0
    j = 0
    wig=root.winfo_children()
    for b in wig:
        b.place_forget()
        resume_button.place_forget()
    start_button.place(x=20,y=300,width=300,height=100)
    lap_button.place(x=660,y=300,width=300,height=100)
    reset_button.place(x=340,y=300,width=300,height=100)
    clock_frame.place(x=200,y=50,width=600,height=200)

def lap():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,i,j
    if i<9:
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)),20+(100*i),400+(j*50))
    else:
        j+=1
        i=0
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)),20+(100*i),400+(j*50))
    i+=1

#Step 5: Creating Buttons. 35:42
#Creating the buttons and widgets.
clock_frame=Label(text="00:00:00",bg="black",fg="blue",font=("default",100,"bold"))
start_button=Button(text="START",bg="green",fg="black",command=start,font=("default",50,"bold"))
stop_button=Button(text="STOP",bg="red",fg="black",command=stop,font=("default",50,"bold"))
resume_button=Button(text="RESUME",bg="green",fg="black",command=start,font=("default",50,"bold"))
lap_button=Button(text="LAP",bg="yellow",fg="black",command=lap,font=("default",50,"bold"))
reset_button=Button(text="RESET",bg="orange",fg="black",command=clear,font=("default",50,"bold"))

#Step 6: Placing The Buttons. 44:18
#Placing the buttons and widgets.
start_button.place(x=20,y=300,width=300,height=100)
lap_button.place(x=660,y=300,width=300,height=100)
reset_button.place(x=340,y=300,width=300,height=100)
clock_frame.place(x=200,y=50,width=600,height=200)

root.mainloop()
