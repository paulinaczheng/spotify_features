import requests
import pandas as pd
import json
#dictionary of artist id's
dict_of_ids = {'marshmello':"64KEffDW9EtZ1y2vBYgq8T", 'pluth':"6VuMaDnrHyPL1p4EHjYLi7",'migos':"6oMuImdp5ZcFhWP0ESe6mG"}
#Key for api's
api_key = "BQCWKwfo0gM_Jk3ddQeiHdlpb9Segs0NVek9XHi3SwMIhJtbJNSQGRb2ADh9tKl_ZXfi5m1ZSQvIKBAzbDeQDxqHyvBr1clYKhg3qNdoFgxJNZ98ohBswUpU_27Q0im4Y-VQTIh6VA"
#Headers for Spotify API
headers = {'Accept': 'application/json',
'Content-Type': 'application/json',
'Authorization': 'Bearer {}'.format(api_key)}
