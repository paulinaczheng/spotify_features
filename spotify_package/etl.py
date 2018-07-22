from spotify_package.api_track_features import *
#converts artist object to artist name
for artist in Artist.query.all():
    if artist.name == 'Migos':
        migos = artist
    elif artist.name == 'Marshmello':
        marshmello = artist
    elif artist.name == 'Charlie Puth':
        puth = artist

def artist_name_by_obj(artist_object):
    for artist in Artist.query.all():
        if artist_object == artist:
            name = artist.name
            return name
#return list of tuples for all artist, track pairs
def all_track_names_artist(top_track=False):
    if top_track==True:
        return [(track.name, artist_name_by_obj(track.artist)) for track in  Track.query.all()
        if track.top_track==True]
    else:
        return [(track.name, artist_name_by_obj(track.artist)) for track in  Track.query.all()
        if track.top_track==False]

def track_obj_by_name(name):
    return [track for track in Track.query.all() if track.name == name][0]

def feature_name_by_id(id):
    return [feature.name for feature in Feature.query.all() if feature.id == id][0]

def pull_track_features_by_track(name):
   obj = track_obj_by_name(name)
   obj_id = obj.id
   return [(feature_name_by_id(trackfeature.feature_id) ,trackfeature.value) for trackfeature in TrackFeature.query.all() if trackfeature.track_id == obj_id]

def tracks_for_artist(artist_name, top_track=False):
    tracks = []
    for pair in all_track_names_artist(top_track):
        if pair[1] == artist_name:
            tracks.append(pair[0])
    return tracks

def all_featurevalue_artist(artist, top_track=False):
    feature_values = []
    artist_tracks = tracks_for_artist(artist, top_track)
    for track in artist_tracks:
        feature_values.append({track:pull_track_features_by_track(track)})
    return feature_values

def feature_values_average(feature, artist):
    dict_values = [value for value in all_featurevalue_artist(artist)]
    feature_values_list = [tup[1] for item in dict_values for value in item.values() for tup in value if tup[0] == feature]
    return sum(feature_values_list)/len(feature_values_list)

def feature_names():
    return [feature.name for feature in Feature.query.all()]

def avg_featurevalues_artist(artist, feature_names_list):
    return {feature: feature_values_average(feature, artist) for feature in feature_names_list}

def avg_featurevalues_artist(artist, feature_names_list):
    return {feature: feature_values_average(feature, artist) for feature in feature_names_list}

# def test():
#     dict_values = [value for value in all_featurevalue_artist(artist)]
#     for item in dict_values:
#         for k, v in item.items():
#             for track in Track.query.all():
#                 if track.name == k:
#                     v.append(('popularity', track.track_popularity))
#     return dict_values

def track_popularity():
    return {track.name: track.track_popularity for track in Track.query.all()}

def create_trace(artist, feature, title, marker, top_track=False):
    dict_values = [value for value in all_featurevalue_artist(artist, top_track)]
    popularity_dict = track_popularity()
    feature_dict = [{'name': key, feature:tuple[1], 'popularity': popularity_dict[key]} for item in dict_values for key,value in item.items() for tuple in value if tuple[0] == feature]
    x = [dict[feature] for dict in feature_dict]
    y = [dict['popularity'] for dict in feature_dict]
    text = [dict['name'] for dict in feature_dict]
    return dict(x=x, y=y, name=title, mode='markers', marker=marker, text=text)

marker1 = dict(
size = 20,
color = 'green',)
marker2 = dict(
size = 20,
color = 'blue',
line = dict(
width = 2,))

def top_track_title(artist, feature):
    return artist + ' ' + 'Top Tracks by ' + feature

def oth_track_title(artist, feature):
    return artist + ' ' + 'Other Tracks by ' + feature

def list_of_traces(artist_name):
    top_track_trace_list = []
    oth_track_trace_list = []
    artist_names = [artist.name for artist in Artist.query.all() if artist.name == artist_name]
    feature_names = [feature.name for feature in Feature.query.all()]
    for artist in artist_names:
        for feature in feature_names:
            top_track_name = top_track_title(artist, feature)
            oth_track_name = oth_track_title(artist, feature)
            top_track_trace_list.append(create_trace(artist, feature, top_track_name , marker1, top_track=True))
            oth_track_trace_list.append(create_trace(artist, feature, oth_track_name, marker2))
    final_trace_list = [top_track_trace_list, oth_track_trace_list]
    return final_trace_list
