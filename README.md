# raceFinder
Helps people find races and details about the race.

This Repository will draw on a few APIs:
RunReg.com,
NWS API,
GeoCode API (this API is throttled)

This is a program that helps people simply search for races to register for and make an informed choice about which race they should sign up for based on the event details and weather data, all compiled in one convenient CSV file.

HOW IT WORKS:
The provided tkinter interface will allows the user to enter some basic race information. This will then be used to search the race registry for races that fit the search terms and returns the top 10 results. (Top 10 was chosen because it takes around 10 minutes to run if all data is returned)

FILES CONTAINED:
interface.py
racesearch.py
runregconnector.py
weatherconnector.py

HOW TO USE:
Open interface.py and run the program to bring up the GUI. Type in your search criteria to see race results. The program will then return a CSV file with information on the top results in a CSV file. You can name this file, or it will name itself as "last_race_search.csv" by default.



LIMITATIONS:
This race registration API seems to have most of its races located in the northeast region. Also, the weather data is a lot to take in, but it can also be very helpful. The links to weather icons and the race info are the most useful returned information. Event types include the distance component, but due to the nature of how these races are inputted, some races are '5km', '5k', '5 k', or '5 km'. This means it may be difficult to search for certain event types, but it is possible.
