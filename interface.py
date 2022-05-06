# Import Tkinter
from tkinter import *
import racesearch as search
import runregconnector, weatherconnector, csv

# Create Tkinter Frame
win = Tk()
win.title("raceFinder")
headers = ['event_name','ZIP','city','state','types','categories','URL','latitude','longitude','Weather']

# Set the size of window!
win.geometry("725x250")

# Define my parameter variables of strings!
region, states, name, eventType, year, fileName = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

# Function for the button command to have that starts the search and export file

def write_file(data, name):
    if name != '':
        file_name = str(name) + ".csv"
    else:
        file_name = "last_race_search.csv"
    file = open(file_name, "w")
    writer = csv.DictWriter(file, fieldnames=headers) # Use dict writer because it gives dictionaries
    writer.writeheader()
    writer.writerows(data)
    print('CSV file successfully created.') # This is used to create a log of successful executions.
    file.close()

def searching():
   global region, states, name, eventType, year, fileName
   parameters = [region.get(), states.get(), name.get(), eventType.get(), year.get()]
   raceData = search.compileRaceData(parameters)
   write_file(raceData, fileName.get())

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

# Entry widget for STATES and its label
statesLabel = Label(win, text="State (XX format, such as 'MA')")
statesLabel.grid(row=3,column=0)
statesEntry = Entry(win, width=35, textvariable=states)
statesEntry.grid(row=3,column=1)

# Entry widget for EVENT NAME and its label
nameLabel = Label(win, text="Event Name")
nameLabel.grid(row=4,column=0)
nameEntry = Entry(win, width=35, textvariable=name)
nameEntry.grid(row=4,column=1)

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