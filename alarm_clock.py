from tkinter import *
import datetime as dt
import time
import pygame

pygame.mixer.init()

def play_alarm_sound():
    pygame.mixer.music.load("sound.wav")
    pygame.mixer.music.play(loops=-1) 

def stop_alarm():
    pygame.mixer.music.stop()



def alarm(setAlarmTimer):
    while True:
        time.sleep(1)
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H:%M:%S")
        the_message = "Current Time: " + str(currentTime)
        print(the_message)
        if currentTime == setAlarmTimer:
            play_alarm_sound()
            break

def getAlarmTime():
    alarmSetTime = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(alarmSetTime)

def snooze():

    stop_alarm()

    time.sleep(300)  

    play_alarm_sound()

guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("500x200")
guiWindow.config(bg="#23272a")
guiWindow.resizable(width=False, height=False)

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="white",
    bg="#23272a",
    font=("Arial", 12)
).place(
    x=0,
    y=170
)

add_time = Label(
    guiWindow,
    text="Hour     Minute     Second",
    font=("Arial", 12),
    fg="white",
    bg="#23272a"
).place(
    x=200,
    y=10
)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm: ",
    fg="white",
    bg="#23272a",
    relief="solid",
    font=("Arial", 13, "bold")
).place(
    x=5,
    y=50
)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="white",
    width=4,
    font=("Arial", 12)
).place(
    x=220,
    y=53
)

minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="white",
    width=4,
    font=("Arial", 12)
).place(
    x=297,
    y=53
)

secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="white",
    width=4,
    font=("Arial", 12)
).place(
    x=374,
    y=53
)

submit = Button(
    guiWindow,
    text="Set The Alarm",
    fg="white",
    bg="#7289da",
    width=15,
    command=getAlarmTime,
    font=("Arial", 12, "bold")
).place(
    x=220,
    y=100
)

snooze_button = Button(
    guiWindow,
    text="Snooze",
    fg="white",
    bg="#ffcc4d",
    width=8,
    command=snooze,
    font=("Arial", 12, "bold")
).place(
    x=220,
    y=135
)

stop_button = Button(
    guiWindow,
    text="Stop",
    fg="white",
    bg="#f04747",
    width=8,
    command=stop_alarm,
    font=("Arial", 12, "bold")
).place(
    x=330,
    y=135
)

guiWindow.mainloop()
