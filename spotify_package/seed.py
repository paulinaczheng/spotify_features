from models import *

# # Artist.query.delete_all()
#
taylor_swift = Artist(name="Taylor Swift", artist_popularity=66, followers=1000)
selena_gomez = Artist(name="Selena Gomez", artist_popularity=11, followers=500)


album1 = Album(name='album1')
album2 = Album(name='album2')

track1 = Track(name='track1', track_popularity=32, album=album1, album_id=album1.id,
artist_id=taylor_swift.id, artist=taylor_swift)
track2 = Track(name='track2', track_popularity=54, album=album2, album_id=album2.id,
artist_id=selena_gomez.id, artist=selena_gomez)

danceability=Feature(name='danceability')
valence=Feature(name='valence')

trackfeature1= TrackFeature(track_id=track1.id, feature_id = danceability.id, value=0.4)
trackfeature2=TrackFeature(track_id=track2.id, feature_id = valence.id, value=0.5)

pop = Genre(name='Pop')
rock = Genre(name='Rock')

playlist1 = Playlist(name='playlist1')
playlist2= Playlist(name='playlist2')

trackgenre1=TrackGenre(track_id = track1.id, genre_id = pop.id)
trackgenre2=TrackGenre(track_id = track2.id, genre_id=rock.id)

artistgenre1=ArtistGenre(artist_id=taylor_swift.id, genre_id=pop.id)
artistgenre2=ArtistGenre(artist_id=taylor_swift.id, genre_id=rock.id)
artistgenre3=ArtistGenre(artist_id=selena_gomez.id, genre_id=pop.id)

playlisttrack1=PlaylistTrack(playlist_id=playlist1.id, track_id=track1.id)
playlisttrack2=PlaylistTrack(playlist_id=playlist1.id, track_id=track2.id)
playlisttrack3=PlaylistTrack(playlist_id=playlist2.id, track_id=track2.id)

, trackfeature1, trackfeature2,
pop, rock, playlist1, playlist2, trackgenre1, trackgenre2, artistgenre1, artistgenre2, artistgenre3, playlisttrack1,
playlisttrack2, playlisttrack3, danceability, valence]


if db.session.query(Artist).all() == []:
    db.session.add(taylor_swift)
    db.session.add(selena_gomez)
    # db.session.commit()

# # print(Artist.query.all())
print([artist.name for artist in Artist.query.all()])
