# runregconnector
# Finding Races, getting from RunReg.com

# Importing modules

import json, os, requests, pprint

# Initializing all possible search terms for this particular API
region, states, distance, eventtype, year = '', '','','',''

pretty_parameter_labels = ['Region', 'State', 'Event Name', 'Event Type', 'Year']
parameter_labels = ['region', 'states', 'name', 'eventtype', 'year']
search_parameters = [region, states, distance, eventtype, year]

def build_url(parameters):
    search_for = ""
    x = 0
    for i in parameters:    # If a parameter is empty, it doesn't search for it. If the parameter contains a value, then it will be added to the search
        search_for += parameter_labels[x] + "=" + parameters[x] + "&"
        x += 1
    base_url = "http://www.RunReg.com/api/search/"
    url = base_url + "?" + search_for
    return url

def send_request(url):
    site_response = requests.get(url)
    site_response.raise_for_status() # checks for errors in the API, whether it is properly functioning or not
    raceJson = json.loads(site_response.text)
    return raceJson