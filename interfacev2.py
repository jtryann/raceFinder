# Import the Tkinter Library
from tkinter import *

# Create an instance of Tkinter Frame
win = Tk()

# Set the geometry of window
win.geometry("700x500")

# Define a String Variable
state = StringVar()

# Define a function to print the Entry widget Input
def printinput(*args):
   print(state.get())

# Create an Entry widget
entry = Entry(win, width=35, textvariable=state)
entry.pack()

# Trace the Input from Entry widget
state.trace("w", printinput)
win.mainloop()