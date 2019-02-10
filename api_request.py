import requests
import json

from brewerydb import *
BreweryDb.configure(API_KEY)

# print(BreweryDb.search({'type':'beer','q':'unibroue'}))
# print(BreweryDb.beers({'page':10}))

# Learning json I/O
#path = '/mnt/c/Users/ryanc/OperationMeteor/brewlocal/brewerydb/all_beers.json'
#parsed = json.loads(path)
#print(json.dumps(parsed, indent=4, sort_keys=True))
