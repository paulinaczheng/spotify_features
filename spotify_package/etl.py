#Create genres for artists
all_genres = []
def find_or_create_genre(genre_list):
    genre_objs = []
    for genre in genre_list:
        for instance in all_genres:
            if genre != instance.name:
                all_genres.append(Genre(name=genre))
                genre_objs.append(Genre(name=genre))
            else:
                genre_objs.append(instance)
    return genre_objs

#Get genre names
def genre_names(all_genres):
    return [genre.name for genre in all_genres]

#Get Several Artists
all_artists = []
def artist(data):
    for item in data:
        name = item['name']
        spotify_id = item['id']
        popularity = item['popularity']
        followers = item['followers']['total']
        genres = item['genres']
        genre_objects = find_or_create_genre(genres)
        all_artists.append(Artist(spotify_id=spotify_id, name=name, popularity=popularity, followers=followers, genres = genre_objects))
    return all_artists

#Get artist top tracks
all_track_ids = []
all_album_ids = []
def artist_top_tracks(data):
    #local variable, artist-dependent
    top_track_names = []
    for item in data:
        top_track_names.append(item['name'])
        all_track_ids.append(item['id'])
        #check to see if album isn't already in all_album_ids list before adding to the list:
        if item['album']['id'] not in all_album_ids:
            all_album_ids.append(item['album']['id'])
    return top_track_names

#Get album tracks
def album_tracks(data):
    for item in data:
        #check if track_id isn't already in all_track_ids before adding to list:
        if item['id'] not in all_track_ids:
            all_track_ids.append(item['id'])
    return all_track_ids #don't need to

#Get first category playlist id
playlist_ids = []
def category_playlist(data):
    if data[0]['id'] not in playlist_ids:
        playlist_ids.append(data[0]['id'])
    return playlist_ids #don't need to

#Get playlist tracks
def playlist_tracks(data):
    for item in data:
        if item['track']['id'] not in all_track_ids:
            all_track_ids.append(item['track']['id'])
    return all_track_ids #don't need to
