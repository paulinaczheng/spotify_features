# from config import *
# from models import *
# from api_artists_genres import *
# from api_top_tracks import *
from api_all_tracks import *

def url_features(a,b):
    merge = '%2C'.join(list_all_tracks()[a:b])
    feature_apis.append("https://api.spotify.com/v1/audio-features" + "?ids=" + merge)
    return feature_apis
url_features(0,50)
url_features(50,100)

def features_dict():
    features_dicts = []
    for url in feature_apis:
        response_features = requests.get(url, headers=headers)
        track_features = json.loads(response_features.content)
        features_dicts.extend(track_features['audio_features'])
    return features_dicts

def feature_objs(feature_list):
    for feature in feature_list:
        all_features.append(Feature(name=feature))
    return all_features

def add_features(all_features):
    for feature in all_features:
        db.session.add(feature)
        db.session.commit()

def feature_values(track_id, feature_list, all_features_dict):
    feature_values_dict = {}
    for feat in feature_list:
        for item in all_features_dict:
            if item['id'] == track_id:
                feature_values_dict[feat] = item[feat]
    return feature_values_dict

def track_features(all_features, all_features_dict, all_track_objs, feature_list):
    for track in all_track_objs:
        for feature in all_features:
            track_id = track.spotify_id
            feature_id = feature.id
            feature_value = feature_values(track_id, feature_list, all_features_dict)
            value = feature_value[feature.name]
            #update everything below here
            track_feature = TrackFeature(track_id=track_id, feature_id=feature_id, value=value)
            feature.track_features.append(track_feature)
            track.track_features.append(track_feature)
            track_features_list.append(track_feature)
    return track_features_list
