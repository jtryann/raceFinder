# raceFinder
Helps people find races and details about the race.

This Repository will draw on a few APIs:
RunReg.com
NWS API
GeoCode API

I'm working on a way for people to gather information about potential races, what the profile of the race is, and providing information to help them sign up, including with what the weather looks like in that location.

HOW IT WORKS:
The provided tkinter interface will allows the user to enter some basic race information. This will then be used to search the race registry for races that fit the search terms and returns the top 10 results. (Top 10 was chosen because it takes around 10 minutes to return all event data)

FILES CONTAINED:
interface.py
racesearch.py
runregconnector.py
weatherconnector.py

HOW TO USE:
Open interface.py and run the program to bring up the GUI. Type in your search criteria to see race results. The program will then return a CSV file with information on the top results in a CSV file. You can name this file, or it will name itself as "last_race_search.csv" by default.
