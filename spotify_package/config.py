import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'biggie':"5me0Irg2ANcsgc93uaYrpb",
'crow':"4TKTii6gnOnUXQHyuo9JaD",'aerosmith':'7Ey4PD4MYsKc5I2dolUwbH',
'carrie': '4xFUf1FHVy696Q1JQZMTRj', 'bee_gees': '1LZEQNv7sE11VDY3SdxQeN',
'fall_out': '4UXqAaa6dQYAk18Lv7PEgX'}

#Key for api's
api_key = "BQDWtzbGZmyeF1AEaSt-5EUJ8rGkmcKwzXpXF2jwlB2jvaZ3916bo2RK4_sPqJQ1HLfwEpJL6cFUo2yrQuCwLL8S8C9GJY4Xlq8fQrgjaroBuiHutQnri-luwNQFpdnn67jQY5A0Gg"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm"]
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","5me0Irg2ANcsgc93uaYrpb"]
rock_list = ['7Ey4PD4MYsKc5I2dolUwbH', '4UXqAaa6dQYAk18Lv7PEgX']
country_list = ["4TKTii6gnOnUXQHyuo9JaD", '4xFUf1FHVy696Q1JQZMTRj']
dance_list = ["64KEffDW9EtZ1y2vBYgq8T", '1LZEQNv7sE11VDY3SdxQeN']

# carrie underwood = 4xFUf1FHVy696Q1JQZMTRj
# bee gees = 1LZEQNv7sE11VDY3SdxQeN
# fall out = 4UXqAaa6dQYAk18Lv7PEgX
# bee gees album id = 3WW11Jf3O3lfFRF5wNMqkn
# carrie album id = 3iLrVuA1k7onNmZTuUQH4u
# fall out album = 6KOWjVP0mh5rOqmzm4tkPD
