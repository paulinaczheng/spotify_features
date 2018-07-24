from spotify_package.api_artists_genres import *

#function get list of API's to call for each artist's top tracks
def url_artist_top_tracks():
    x=[id for id in dict_of_ids.values()]
    return ["https://api.spotify.com/v1/artists/{id}/top-tracks".format(id=artist_id)+'?country=US' for artist_id in x]

#function to get list of dictionaries with each artist's top tracks (all coming from dict of artist id's)
def top_tracks_dict():
    list_dicts = []
    for url in url_artist_top_tracks():
        response_artists = requests.get(url, headers=headers)
        track_dict = json.loads(response_artists.content)
        list_dicts.extend(track_dict['tracks'])
    return list_dicts

top_tracks_dict = top_tracks_dict()
# track_artist_dict = track_artists(data, song_id)
#Get artist top tracks
all_track_ids = []
all_album_ids = []
def artist_top_tracks(top_tracks_dict):
    #local variable, artist-dependent
    top_track_ids = []
    for item in top_tracks_dict:
        top_track_ids.append(item['id'])
        all_track_ids.append(item['id'])
        #check to see if album isn't already in all_album_ids list before adding to the list:
        all_album_ids.append(item['album']['id'])
        # song_id = item['id'] #change name to id here
    return top_track_ids

def check_top_track(top_tracks, spotify_id):
    if spotify_id in top_tracks:
        return True
    else:
        return False

top_tracks = artist_top_tracks(top_tracks_dict)
#create dictionary of albums and frequency, returning top 2
def album_freq(all_album_ids):
    album_freq_dict = [{'id': album, 'freq': all_album_ids.count(album)} for album in set(all_album_ids)]
    return sorted(album_freq_dict, key=lambda k: k['freq'], reverse=True)[0:2]

#urls for get album API's for each album id
def url_album_ids():
    list_album_ids = [album['id'] for album in album_freq(all_album_ids)]
    list_album_ids.append('7dRdaGSxgcBdJnrOviQRuB') #append Biggie smalls
    list_album_ids.append('0xi4cOWPUHjctyYU8ypCOB') #append Marshmello album
    list_album_ids.append('1tuM8yBePaekEruGsH2J79') #append aerosmith
    list_album_ids.append('52E4RP7XDzalpIrOgSTgiQ') #append mj
    list_album_ids.append('3w7TTi80vZApF0rQE5DMYb') #append crow
    list_album_ids.append('3WW11Jf3O3lfFRF5wNMqkn') #append bee gees
    list_album_ids.append('3iLrVuA1k7onNmZTuUQH4u') #append carrie
    list_album_ids.append('6KOWjVP0mh5rOqmzm4tkPD') #append fall out boy
    merge = '%2c'.join(list_album_ids)
    return "https://api.spotify.com/v1/albums"+ "?ids=" + merge

#to call API for all albums
response_albums = requests.get(url_album_ids(), headers=headers)
albums_raw = json.loads(response_albums.content)
albums_clean = [album for album in albums_raw['albums']]
#dictionary with keys as Album name and values as list of tracks
album_tracks_dict = {album['name']:album['tracks'] for album in albums_clean}

all_albums = []
def list_all_tracks():
    all_song_id_list = []
    for track in album_tracks_dict.values():
        song_ids_per_album = [item['id'] for item in track['items']]
        all_song_id_list.extend(song_ids_per_album)
    all_track_ids.extend(all_song_id_list)
    return list(set(all_track_ids))
