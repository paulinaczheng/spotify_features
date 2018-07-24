from spotify_package.config import *
from spotify_package.models import *
#function to format all artist id's properly for API
def url_of_artist_ids():
    x=[id for id in dict_of_ids.values()]
    merge = '%2C'.join(x)
    return "https://api.spotify.com/v1/artists" + "?ids=" + merge

response_artists = requests.get(url_of_artist_ids(), headers=headers)
artists_raw = json.loads(response_artists.content)
artists_clean = [artist for artist in artists_raw['artists']]

#call all genres api
def get_all_genres():
    url_genres_all = 'https://api.spotify.com/v1/browse/categories?country=US'
    response_genres = requests.get(url_genres_all, headers=headers)
    genres_raw = json.loads(response_genres.content)
    return [Genre(name=genre['id']) for genre in genres_raw['categories']['items']]

all_genres = get_all_genres()

#Create genres for artists
def genre_artist(spotify_id):
    if spotify_id in dance_list:
        genre = 'edm_dance'
    elif spotify_id in pop_list:
        genre = 'pop'
    elif spotify_id in hiphop_list:
        genre = 'hiphop'
    elif spotify_id in country_list:
        genre = 'country'
    elif spotify_id in rock_list:
        genre = 'rock'
    return genre

def find_or_create_genre(genre_name):
    for item in all_genres:
        if genre_name == item.name:
            return item

all_artists = []
