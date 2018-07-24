from spotify_package.api_top_tracks import *
#Headers for Spotify API

list_of_apis = []
def url_of_track_ids(a,b):
    merge = '%2C'.join(list_all_tracks()[a:b])
    list_of_apis.append("https://api.spotify.com/v1/tracks" + "?ids=" + merge)
    return list_of_apis
url_of_track_ids(0,50)
url_of_track_ids(50,100)
url_of_track_ids(100,150)
url_of_track_ids(150,200)
url_of_track_ids(200,250)

#to call API for all tracks
final_all_tracks = []
for url_list in list_of_apis:
    response_all_tracks = requests.get(url_list, headers=headers)
    all_tracks_raw = json.loads(response_all_tracks.content)
    all_tracks_clean = [track for track in all_tracks_raw['tracks']]
    final_all_tracks.extend(all_tracks_clean)

song_name_artists = {track['id']:[artist['name'] for artist in track['artists']] for track in final_all_tracks}
song_name_artists['0nhVrTiCGiGRCoZOJiWzm1'][0] = 'Migos_Filler'

track_artist = []
 #for every track, their artist
#returns list of songs with a featured artist
def track_feature(song_name_artists):
    songs_with_feat_artist = []
    for key,value in song_name_artists.items():
        if len(value) > 1:
            songs_with_feat_artist.append(key)
        track_artist.append((key, value[0]))
    return songs_with_feat_artist

songs_with_feat_artist = track_feature(song_name_artists)

def check_featured_artist(songs_with_feat_artist, spotify_id):
    for track in songs_with_feat_artist:
        if track == spotify_id:
            return True
        else:
            return False

def check_artist(spotify_id, track_artist, all_artists):
    for item in track_artist:
        if item[0] == spotify_id:
            for artist in all_artists:
                if item[1] == artist.name:
                    return artist

def return_artist_id(artist):
    if artist is None:
        return None
    else:
        return artist.id

def return_artist_genre(artist):
    if artist is None:
        return None
    else:
        return artist.genre

def return_genre_id(genre):
    if genre is None:
        return None
    else:
        return genre.id

all_track_objs = []
