# from spotify_package.api_track_features import *
#
# # Artists and Genres
# # Get Several Artists
# def artist(data):
#     for item in data:
#         name = item['name']
#         spotify_id = item['id']
#         popularity = item['popularity']
#         followers = item['followers']['total']
#         genre_name = genre_artist(spotify_id)
#         genre = find_or_create_genre(genre_name)
#         all_artists.append(Artist(spotify_id=spotify_id, name=name, artist_popularity=popularity, followers=followers, genre = genre))
#     return all_artists
#
# def add_artists(all_artists):
#     for artist in all_artists:
#         db.session.add(artist)
#         db.session.commit()
#
# def add_genres(all_genres):
#     for genre in all_genres:
#         db.session.add(genre)
#         db.session.commit()
#
# artist(artists_clean)
# add_artists(all_artists)
# add_genres(all_genres)
#
# #Top Tracks
# #Top Tracks and Albums
# #Get album tracks
# def albums(albums_clean):
#     for album in albums_clean:
#         artist = [artist for artist in all_artists if artist.spotify_id == album['artists'][0]['id']][0]
#         artist_id = artist.id
#         all_albums.append(Album(spotify_id=album['id'], name=album['name'], release_date=album['release_date'], artist = artist, artist_id = artist_id))
#     return all_albums
#
# def add_albums(all_albums):
#     for album in all_albums:
#         db.session.add(album)
#         db.session.commit()
#
#
# albums(albums_clean)
# add_albums(all_albums)
#
# #All Tracks
#
# def track_objects(final_all_tracks, track_artist, all_artists):
#     for track in final_all_tracks:
#         spotify_id = track['id']
#         name = track['name']
#         track_popularity = track['popularity']
#         featured_artist = check_featured_artist(songs_with_feat_artist, spotify_id)
#         top_track = check_top_track(top_tracks, spotify_id)
#         artist = check_artist(spotify_id,track_artist, all_artists)
#         artist_id = return_artist_id(artist)
#         genre = return_artist_genre(artist)
#         genre_id = return_genre_id(genre)
#         all_track_objs.append(Track(spotify_id=spotify_id, name=name, track_popularity=track_popularity, featured_artist=featured_artist, top_track=top_track, artist=artist, artist_id=artist_id, genre=genre, genre_id=genre_id))
#     return all_track_objs
#
# #All tracks
# def add_track_objects(all_track_objs):
#     for track in all_track_objs:
#         db.session.add(track)
#         db.session.commit()
#
# track_objects(final_all_tracks, track_artist, all_artists)
# add_track_objects(all_track_objs)
#
# #Track Features
# def feature_objs(feature_list):
#     for feature in feature_list:
#         all_features.append(Feature(name=feature))
#     return all_features
#
# def add_features(all_features):
#     for feature in all_features:
#         db.session.add(feature)
#         db.session.commit()
#
# def track_features(all_features, all_features_dict, all_track_objs, feature_list):
#     for track in all_track_objs:
#         for feature in all_features:
#             track_id = track.spotify_id
#             feature_id = feature.id
#             feature_value = feature_values(track_id, feature_list, all_features_dict)
#             value = feature_value[feature.name]
#             #update everything below here
#             track_feature = TrackFeature(track_id=track_id, feature_id=feature_id, value=value)
#             feature.track_features.append(track_feature)
#             track.track_features.append(track_feature)
#             track_features_list.append(track_feature)
#     return track_features_list
#
# def add_track_features(track_features_list):
#     for track_feature in track_features_list:
#         db.session.add(track_feature)
#         db.session.commit()
#
#
# feature_objs(feature_list)
# add_features(all_features)
# track_features(all_features, all_features_dict, all_track_objs, feature_list)
# add_track_features(track_features_list)
