from tkinter import *
import os

def SHUTDOWN_COMPUTER():
    return os.system("shutdown /s /t 1")

def RESTART_COMPUTER():
    return os.system("shutdown /r /t 1")

Sparsh_Root = Tk()
Sparsh_Root.title("SHUTDOWN and RESTART")

TITLE_LABEL = Label(Sparsh_Root, text = "What do you want the computer to do?", font = ('Bahnschrift 25 bold underline'))
TITLE_LABEL.pack()

SHUTDOWN_BUTTON = Button(Sparsh_Root, text = "SHUTDOWN", bg = 'red', fg = 'black', activebackground = 'blue', font = ('Bahnschrift', 15), command = SHUTDOWN_COMPUTER)
SHUTDOWN_BUTTON.pack()

RESTART_BUTTON = Button(Sparsh_Root, text = "RESTART", bg = 'red', fg = 'black', activebackground = 'blue', font = ('Bahnschrift', 15), command = RESTART_COMPUTER)
RESTART_BUTTON.pack()


Sparsh_Root.mainloop()
