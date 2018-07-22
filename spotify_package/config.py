import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}
#Key for api's
api_key = "BQCjX5vu1DBqFUqbxsIYReSVupmvkrf6tps1YPJ9TKO0E1C-wZ9DDeBFKmwCI2mdVdJ_1FY_NCvJOyiLNZOKU29UpZ7aFc3hN97fPTxNrf5gaKqbgtUDPtAckPn4nHl2p5jjQVvaPQ"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}
