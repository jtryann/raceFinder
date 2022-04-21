# This file collects user inputs, displays race and weather info, and displays in tkinter

import runregconnector as race, weatherconnector as weather, pprint

name, region, states, distance, eventtype, year, startDate, endDate, startpage = '', '','','','','','','',''

pretty_parameter_labels = ['Race Name', 'Region', 'State', 'Race Distance', 'Event Type', 'Year', 'Search Start Date', 'Search End Date', 'Results Page #']
parameter_labels = ['name', 'region', 'state', 'distance', 'eventtype', 'year', 'startDate', 'endDate', "startpage"]
search_parameters = [name, region, states, distance, eventtype, year, startDate, endDate, startpage]

def sortRaceData():
    raceData = race.send_request(race.build_url(search_parameters))
    matchingEvents = raceData['MatchingEvents']
    eventsData = {}
    for i in matchingEvents:
        eventsData['event_name'] = i.get('EventName')
        eventsData['ZIP'] = i.get('EventZip')
        eventsData['city'] = i.get('EventCity')
        eventsData['state'] = i.get('EventState')
        eventsData['types'] = i.get('EventTypes')
        eventsData['categories'] = i.get('Categories')
        eventsData['URL'] = i.get('EventUrl')
    return eventsData

# Write file
def write_file(data):
    file_name = "last_race_search.txt"
    file = open(file_name, "w")
    file.write(str(data))
    file.close()