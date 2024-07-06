# import the necessary modules
from threading import Timer
import time
import tkinter as tk
from tkinter import *
from datetime import datetime
import winsound
from win10toast import ToastNotifier

# create the countdown function
def countdown():
    t = count.get()
    while t:
        mins, secs = divmod(t, 60)
        display = ('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)  # sleep for 1 second
        t -= 1
        Label(window, text=display).pack()

    Label(window, text="Time-Up", font=('bold', 20)).place(x=250, y=290)

# create the main window
window = Tk()
window.geometry('600x600')
window.title('PythonGeeks')

# declare the variables
hour = StringVar()
minus = StringVar()
secon = StringVar()
check = BooleanVar()

# create the UI elements
head = Label(window, text="Countdown Clock and Timer", font=('Calibri 15'))
head.pack(pady=20)

Label(window, text="Enter time in HH:MM:SS", font=('bold')).pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minus, width=30).pack()
Entry(window, textvariable=secon, width=30).pack()

Checkbutton(text='Check for Music', onvalue=True, variable=check).pack()

Button(window, text="Set Countdown", command=countdown, bg='yellow').place(x=260, y=230)

# print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window, text=current_time).pack()

# display notification on desktop
toast = ToastNotifier()
toast.show_toast("Notification", "Timer is Off", duration=20, icon_path=None, threaded=True)

# play beep sound if check is True
if check.get():
    winsound.Beep(440, 1000)

# update the window
window.update()
window.mainloop()
