import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG",'mj':"3fMbdgg4jU18AjLCKBhRSm", 'biggie':"5me0Irg2ANcsgc93uaYrpb",'crow':"4TKTii6gnOnUXQHyuo9JaD",'aerosmith':'7Ey4PD4MYsKc5I2dolUwbH'}

#Key for api's
api_key = "BQBjvGZdwFwlA4ltlq9iM0o2tRtqg5YhTg0lkXVJSKPFBiAV0uCS4KlRKZfdwUA5WjprzTb8X94fyxTDhScXr_LQVgQ8qqFmVbyn8GCqxJynrgWLMZQ8uNewQoO63IZAq0FtDpixNw"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}

pop_list = ["6VuMaDnrHyPL1p4EHjYLi7","3fMbdgg4jU18AjLCKBhRSm"]
hiphop_list = ["6oMuImdp5ZcFhWP0ESe6mG","5me0Irg2ANcsgc93uaYrpb"]
rock_list = ['7Ey4PD4MYsKc5I2dolUwbH']
country_list = ["4TKTii6gnOnUXQHyuo9JaD"]

# carrie underwood = 4xFUf1FHVy696Q1JQZMTRj
# bee gees = 1LZEQNv7sE11VDY3SdxQeN
# fall out = 4UXqAaa6dQYAk18Lv7PEgX
# bee gees album id = 3WW11Jf3O3lfFRF5wNMqkn
# carrie album id = 3iLrVuA1k7onNmZTuUQH4u
# fall out album = 6KOWjVP0mh5rOqmzm4tkPD
