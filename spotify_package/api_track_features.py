# from config import *
# from models import *
# from api_artists_genres import *
# from api_top_tracks import *
from spotify_package.api_all_tracks import *

feature_apis = []
def url_features(a,b):
    merge = '%2C'.join(list_all_tracks()[a:b])
    feature_apis.append("https://api.spotify.com/v1/audio-features" + "?ids=" + merge)
    return feature_apis
url_features(0,50)
url_features(50,100)
url_features(100,150)
url_features(150,200)

def features_dict():
    features_dicts = []
    for url in feature_apis:
        response_features = requests.get(url, headers=headers)
        track_features = json.loads(response_features.content)
        features_dicts.extend(track_features['audio_features'])
    return features_dicts

all_features_dict = features_dict()
feature_list = ['danceability', 'energy', 'acousticness', 'valence', 'tempo']
all_features = []


def feature_values(track_id, feature_list, all_features_dict):
    feature_values_dict = {}
    for feat in feature_list:
        for item in all_features_dict:
            if item['id'] == track_id:
                feature_values_dict[feat] = item[feat]
    return feature_values_dict

track_features_list = []
