# runregconnector
# Finding Races, getting from RunReg.com

# Importing modules

import json, os, requests, pprint

name, region, states, distance, eventtype, year, startDate, endDate = 'test'

search_types = {'Race Name', 'Region', 'States', 'Race Distance', 'Event Type', 'Year', 'Search Start Date', 'Search End Date'}
search_parameters = {name, region, states, distance, eventtype, year, startDate, endDate}


def input_parameters():
    for i in search_types:
        search_for = input('Would you like to search by ' + i + '?' )
        if search_for.lower().startswith('y') is True:
            1 == 1

def compile_parameters(parameters):
    1 == 1 

def build_request():
    base_url = "http://www.RunReg.com/api/search/"
    complete_url = base_url + "?"

# Main program
input_parameters()
print(name + ' name')
print(distance + ' distance')
print(endDate + ' endDate')