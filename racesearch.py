from itertools import count
import runregconnector as race, weatherconnector as weather, pprint

name, region, states, distance, eventtype, year, startDate, endDate, startpage = '', '','','','','','','',''

pretty_parameter_labels = ['Region', 'State', 'Race Distance', 'Event Type', 'Year', 'Search Start Date', 'Search End Date']
parameter_labels = ['region', 'state', 'distance', 'eventtype', 'year', 'startDate', 'endDate']
search_parameters = [region, states, distance, eventtype, year, startDate, endDate]
states = 'GA'

# def addWeather(ZIP):
#     weather.getWeather(weather.findGrid(latitude, longitude))

def compileRaceData():
    raceData = race.send_request(race.build_url(search_parameters))
    matchingEvents = raceData['MatchingEvents']
    eventData = {}
    events = [] # stores each race info as a dictionary in a list
    counter = 0 # counts how many loops run (so it doesn't return ALL of the race data)
    for i in matchingEvents:
        eventData = {}
        eventData['event_name'] = i.get('EventName')
        eventData['ZIP'] = i.get('EventZip')
        if len(eventData['ZIP']) != 5: # replaces invalid ZIP codes with an error ZIP (Sorry Canada)
            eventData['ZIP'] = 11111
        eventData['city'] = i.get('EventCity')
        eventData['state'] = i.get('EventState')
        eventData['types'] = i.get('EventTypes')
        eventData['categories'] = i.get('Categories')
        eventData['URL'] = i.get('EventUrl')     
        if eventData['ZIP'] != 11111: # if invalid ZIP code, do not add race to list and get weather data
            try:
                latitude, longitude, = weather.convertZIP(eventData['ZIP'])
                eventData['Weather'] = weather.getWeather(weather.findGrid(latitude, longitude))
            except:
                pass
            events.append(eventData)
        counter += 1
        if counter > 10:
            return events # releases event Data from the top 10 races in list format
        return events

# Write file
def write_file(data):
    file_name = "last_race_search.txt"
    file = open(file_name, "w")
    file.write(str(data))
    file.close()

write_file(compileRaceData())