# Import Tkinter
from tkinter import *

# Create Tkinter Frame
win = Tk()

# Set the size of window!
win.geometry("725x200")

# Define my parameter variables of strings!
region, state, distance, eventType, year = StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
parameters = [region, state, distance, eventType, year]

# Define a function to print the Entry widget Input
def printinput(*args):
    global parameters
    parameters
    print(parameters)

# Creating Title
titletext = "raceFinder"
title = Label(win, text=titletext, font=28)
title.grid(row=0,column=0, columnspan=2)

# Description label
desc_text = "Welcome to raceFinder! Enter search terms below to be returned with a csv of the top 10 results, their race, location, and weather info!"
description = Label(win, text=desc_text)
description.grid(row=1,column=0, columnspan=2)

# Entry widget for REGION and its label
regionLabel = Label(win, text="Region")
regionLabel.grid(row=2,column=0)
regionEntry = Entry(win, width=35, textvariable=region)
regionEntry.grid(row=2,column=1)
region.get()

# Entry widget for STATE and its label
stateLabel = Label(win, text="State")
stateLabel.grid(row=3,column=0)
stateEntry = Entry(win, width=35, textvariable=state)
stateEntry.grid(row=3,column=1)
state.get()

# Entry widget for DISTANCE and its label
distanceLabel = Label(win, text="Distance")
distanceLabel.grid(row=4,column=0)
distanceEntry = Entry(win, width=35, textvariable=distance)
distanceEntry.grid(row=4,column=1)
distance.get()

# Entry widget for EVENT TYPE and its label
eventTypeLabel = Label(win, text="Event Type")
eventTypeLabel.grid(row=5,column=0)
eventTypeEntry = Entry(win, width=35, textvariable=eventType)
eventTypeEntry.grid(row=5,column=1)
eventType.get()

# Entry widget for YEAR and its label
yearLabel = Label(win, text="Year")
yearLabel.grid(row=6,column=0)
yearEntry = Entry(win, width=35, textvariable=year)
yearEntry.grid(row=6,column=1)
year.get()

# Button printing all entry variables
printButton = Button(win,width=35, text="Search and Create CSV", command=printinput, cursor="dot")
printButton.grid(row=7,column=1)

# Trace the Input from Entry widget
win.mainloop()