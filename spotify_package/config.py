import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}
#Key for api's
api_key = "BQBhCOjSbOLBcPu0v6-4WAdJvsXCRhTtkEyx6D4wv74uXkZ0x4tPM0EWsnUEAo3kE95Lo9cKSfGv_yHuQBc0LGHDNib5oRhwBFSEvFVIaMrh6e1fjhZvwQrzmQyCjXR17lSFBx6V0A"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}
