import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}
#Key for api's
# api_key = "BQAb7okRwZCKsocZXQ5-UVNiz4uPEq7-eGkZqP5yqaCu9Wsx9ZUN9BqDpMBDF4VwL4sSaCLb3iLq3S9SCdAeBzipCDTKQCRlNlz3VcGHOLNAt3EnIKUXPczUDKdRV5dKby1xXGbBLg"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format("BQAb7okRwZCKsocZXQ5-UVNiz4uPEq7-eGkZqP5yqaCu9Wsx9ZUN9BqDpMBDF4VwL4sSaCLb3iLq3S9SCdAeBzipCDTKQCRlNlz3VcGHOLNAt3EnIKUXPczUDKdRV5dKby1xXGbBLg")}
