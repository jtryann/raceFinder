# Import Tkinter
from tkinter import *
import racesearch as search

# Create Tkinter Frame
win = Tk()

# Set the size of window!
win.geometry("725x250")

# Define my parameter variables of strings!
region, state, distance, eventType, year, fileName = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

# Define a function to print the Entry widget Input
def printinput(*args):
   global region, state, distance, eventType, year, fileName
   parameters = [region.get(), state.get(), distance.get(), eventType.get(), year.get()]
   print(parameters)

def searching():
   global region, state, distance, eventType, year, fileName
   parameters = [region.get(), state.get(), distance.get(), eventType.get(), year.get()]
   search.write_file(search.compileRaceData(parameters),fileName.get())

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

# Entry widget for STATE and its label
stateLabel = Label(win, text="State")
stateLabel.grid(row=3,column=0)
stateEntry = Entry(win, width=35, textvariable=state)
stateEntry.grid(row=3,column=1)

# Entry widget for DISTANCE and its label
distanceLabel = Label(win, text="Distance")
distanceLabel.grid(row=4,column=0)
distanceEntry = Entry(win, width=35, textvariable=distance)
distanceEntry.grid(row=4,column=1)

# Entry widget for EVENT TYPE and its label
eventTypeLabel = Label(win, text="Event Type")
eventTypeLabel.grid(row=5,column=0)
eventTypeEntry = Entry(win, width=35, textvariable=eventType)
eventTypeEntry.grid(row=5,column=1)

# Entry widget for YEAR and its label
yearLabel = Label(win, text="Year")
yearLabel.grid(row=6,column=0)
yearEntry = Entry(win, width=35, textvariable=year)
yearEntry.grid(row=6,column=1)

# Entry widget for FILENAME and its label
fileNameLabel = Label(win, text="Output File Name")
fileNameLabel.grid(row=7,column=0)
fileNameEntry = Entry(win, width=35, textvariable=fileName)
fileNameEntry.grid(row=7,column=1)

# Button printing all entry variables
printButton = Button(win,width=35, text="Search and Create CSV", command=searching, cursor="dot")
printButton.grid(row=8,column=1)

# Trace the Input from Entry widget
win.mainloop()