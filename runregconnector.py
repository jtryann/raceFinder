# runregconnector
# Finding Races, getting from RunReg.com

# Importing modules

import json, os, requests, pprint

# Initializing all possible search terms for this particular API
name, region, states, distance, eventtype, year, startDate, endDate, startpage = '', '','','','','','','',''

url = "" # url is a global because we may want to use the build_url function or send_request function in one of our other files without using both

pretty_parameter_labels = ['Race Name', 'Region', 'State', 'Race Distance', 'Event Type', 'Year', 'Search Start Date', 'Search End Date', 'Results Page #']
parameter_labels = ['name', 'region', 'state', 'distance', 'eventtype', 'year', 'startDate', 'endDate', "startpage"]
search_parameters = [name, region, states, distance, eventtype, year, startDate, endDate, startpage]

# def input_parameters():
#     for i in search_parameter_labels:
#         search_for = input('Would you like to search by ' + i + '?' )
#         if search_for.lower().startswith('y') is True:
#             1 == 1

def build_url(parameters):
    x = 0
    search_for = ""
    for i in parameters:    # If a parameter is empty, it doesn't search for it. If the parameter contains a value, then it will be added to the search
        if i != "":
            search_for += parameter_labels[x] + "=" + parameters[x] + "&"
            x += 1
    base_url = "http://www.RunReg.com/api/search/"
    global url 
    url = base_url + "?" + search_for

def send_request():
    site_response = requests.get(url)
    site_response.raise_for_status() # checks for errors in the API, whether it is properly functioning or not
    raceJson = json.loads(site_response.text)
    print(raceJson)

# Main program
build_url(search_parameters)
send_request()