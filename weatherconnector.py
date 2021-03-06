# Weather connector
# finding weather based on race location
# NWS (US National Weather Service) API will be used for weather data
# ZIP Code Geocode API to lat/long API used to convert ZIP codes from the racereg API to the weather API

import json, requests, pprint

# functions!
def convertZIP(zipcode): # converts ZIP code into Lat/Long
    location_url = 'https://geocode.xyz/' + str(zipcode) + '}?json=1&region=US'
    response_zip = requests.get(location_url)
    response_zip.raise_for_status()
    location = json.loads(response_zip.text)
    latitude = location["latt"]
    longitude = location["longt"]
    latlong = [latitude, longitude]
    return latlong

 # This function part searches for the 2.5km grid that the NWS splits the US into, and that the ZIP code is located in
def findGrid(latlong):
    latitude = latlong[0]
    longitude = latlong[1]
    grid_url = 'https://api.weather.gov/points/' + str(latitude) + ',' + str(longitude)
    response_grid = requests.get(grid_url)
    response_grid.raise_for_status()
    grid_location = json.loads(response_grid.text)
    nws_office = grid_location['properties']['cwa'] # selects NWS office for locale
    x_grid = grid_location['properties']['gridX'] # selects grid X coordinate
    y_grid = grid_location['properties']['gridY'] # selects grid Y coordinate
    officeData = [nws_office, x_grid, y_grid]
    return officeData

# Finally, now we can get the weather!
def getWeather(officeData):
    office = officeData[0]
    gridX = officeData[1]
    gridY = officeData[2]
    weather_url = 'https://api.weather.gov/gridpoints/'+ office + '/' + str(gridX) + ','+ str(gridY) + '/forecast'
    response_weather = requests.get(weather_url)
    jsondata = json.loads(response_weather.text)
    weatherdata = jsondata['properties']
    forecastdata = weatherdata['periods']
    sorteddata = []
    for i in range(14):
        tempdict = {}
        tempdict['timeframe'] = forecastdata[i]['name']
        tempdict['temperature'] = forecastdata[i]['temperature']
        tempdict['windSpeed'] = forecastdata[i]['windSpeed']
        tempdict['windDirection'] = forecastdata[i]['windDirection']
        tempdict['forecast'] = forecastdata[i]['shortForecast']
        tempdict['icon'] = forecastdata[i]['icon']
        sorteddata.append(tempdict)
    return sorteddata