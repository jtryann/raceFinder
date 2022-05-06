import runregconnector as race, weatherconnector as weather, pprint, csv

def compileRaceData(parameters):
    print('Parameters: ' + str(parameters))
    raceData = race.send_request(race.build_url(parameters))
    matchingEvents = raceData['MatchingEvents']
    print('Matching events: ' + str(len(matchingEvents)))
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
        eventData['latitude'] = i.get('Latitude')
        eventData['longitude'] = i.get('Longitude')
        latitude, longitude = eventData['latitude'], eventData['longitude']
        if latitude != '' and longitude != '': # if the race info has a latitude and longitude, get weather
            try:
                latlong = latitude, longitude
                eventData['Weather'] = weather.getWeather(weather.findGrid(latlong))
            except:
                pass
        elif eventData['ZIP'] != 11111: # if invalid ZIP code, do not add race to list and get weather data
            try:
                latitude, longitude = weather.convertZIP(eventData['ZIP'])
                latlong = latitude, longitude
                eventData['Weather'] = weather.getWeather(weather.findGrid(latlong))
            except:
                pass
        events.append(eventData)
        counter += 1
        if counter > 10 or counter == len(matchingEvents): # return no more than 10 events (due to throttling)
            return events # releases event Data from the top 10 races in list format
