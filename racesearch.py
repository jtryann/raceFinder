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
    for i in matchingEvents:
        eventData = {}
        eventData['event_name'] = i.get('EventName')
        eventData['ZIP'] = i.get('EventZip')
        if len(eventData['ZIP']) != 5: # replaces invalid ZIP codes with an invalid ZIP (Sorry Canada)
            eventData['ZIP'] = 11111
        eventData['lat'] = i.get('Latitude')
        eventData['long'] = i.get('Longitude')
        eventData['city'] = i.get('EventCity')
        eventData['state'] = i.get('EventState')
        eventData['types'] = i.get('EventTypes')
        eventData['categories'] = i.get('Categories')
        eventData['URL'] = i.get('EventUrl')     
        if eventData['ZIP'] != 11111: # if invalid ZIP code, do not add race to list and get weather data
            eventData['Weather'] = weather.getWeather(weather.findGrid(eventData['lat'], eventData['long']))
            events.append(eventData)
    return events # releases event Data from the top 100 races in list format


# Write file
def write_file(data):
    file_name = "last_race_search.txt"
    file = open(file_name, "w")
    file.write(str(data))
    file.close()

write_file(compileRaceData())