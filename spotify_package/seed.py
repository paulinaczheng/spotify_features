from api_track_features import *
from config import *
#Artists and Genres



#Track Features
def add_track_features(track_features_list):
    for track_feature in track_features_list:
        db.session.add(track_feature)
        db.session.commit()

feature_apis = []
all_features_dict = features_dict()
feature_list = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
all_features = []
feature_objs(feature_list)
add_features(all_features)
track_features_list = []
track_features(all_features, all_features_dict, all_track_objs, feature_list)
add_track_features(track_features_list)
