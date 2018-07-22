import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}
#Key for api's
api_key = "BQB-qwfi2BFtruQCbgyoTqj0sJgu33_QN0pnX756bWLSRHmxmL-aMR7akjwBLkPZmCVD5Ko9v9eka1gpSYhd1Sp7I6K5spN7O6c-nPXQTS2kbteTEJXxoll15uwXGeLHcA3EF_Ywfw"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}
