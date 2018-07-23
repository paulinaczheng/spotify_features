import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'biggie':"5me0Irg2ANcsgc93uaYrpb",'crow':"4TKTii6gnOnUXQHyuo9JaD",'aerosmith':'7Ey4PD4MYsKc5I2dolUwbH'}

#Key for api's
api_key = "BQDIS1_BjeFxVaVWwA_9uo9fnEV6WF2ytYBMfYX60pEMLZUNrdagbjkBHqcS4_OC7wbTWUqm9BAtqkQISkdGCSsZzaweStkhUWqUHeJFrgzCHZCf6xenZtDBAzww7pCvqzul5r2mfg"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm","4nDoRrQiYLoBzwC5BhVJzF",'66CXWjxzNUsdJxJ2JdwvnR']
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","5me0Irg2ANcsgc93uaYrpb"]
rock_list = ['7Ey4PD4MYsKc5I2dolUwbH']
country_list = ["4TKTii6gnOnUXQHyuo9JaD"]
