# This file collects user inputs, displays race and weather info, and displays in tkinter

import runregconnector as race, weatherconnector as weather, pprint, requests, time, tkinter

name, region, states, distance, eventtype, year, startDate, endDate, startpage = '', '','','','','','','',''

pretty_parameter_labels = ['Race Name', 'Region', 'State', 'Race Distance', 'Event Type', 'Year', 'Search Start Date', 'Search End Date', 'Results Page #']
parameter_labels = ['name', 'region', 'state', 'distance', 'eventtype', 'year', 'startDate', 'endDate', "startpage"]
search_parameters = [name, region, states, distance, eventtype, year, startDate, endDate, startpage]


raceData = race.send_request(race.build_url(search_parameters))
matchingEvents = raceData['MatchingEvents']
eventsData = {}

for i in matchingEvents:
    myDict = {}
    myDict['event_name'] = i.get('')


# Write file
def write_file(data):
    file_name = "last_race_search.txt"
    file = open(file_name, "w")
    file.write(str(data))
    file.close()

print(len(matchingEvents))