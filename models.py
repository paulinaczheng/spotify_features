class Artist(db.Model):
    __tablename__= 'artists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    artist_popularity = db.Column(db.Integer, nullable=False)
    tracks = db.relationship('Track', back_populates='artist')
    albums = db.relationship('Album', back_populates='artist')
    genres = db.relationship('Genre', secondary='artist_genres', back_populates='artists')

class Track(db.Model):
    __tablename__ = 'tracks '
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    track_popularity = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.Date, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))
    album = db.relationship('Album', back_populates='tracks')
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates='tracks')
    features = db.relationship('Feature', secondary='track_features', back_populates='tracks')
    playlists = db.relationship('Playlist', secondary='playlist_tracks', back_populates='tracks')
    genres = db.relationship('Genre', secondary='track_genres', back_populates='tracks')

class Feature(db.Model):
    __tablename__ = 'features'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    tracks = db.relationship('Track', secondary='track_features', back_populates='features')

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    tracks = db.relationship('Track', back_populates='album')
    artist_id = db.Column(db.Integer, ForeignKey('artists.id'))
    artist = db.relationship('Artist', back_populates='albums')

class Playlist(db.Model):
    __tablename__= 'playlists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genre = db.relationship('Genre', back_populates='playlists')
    tracks = db.relationship('Track', secondary='playlist_tracks', back_populates='playlists')

class Genre(db.Model):
    __tablename__= 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(100), nullable=False)
    playlists = db.relationship('Playlist', back_populates='genre')
    artists = db.relationship('Artist', secondary='artist_genres', back_populates='genres')
    songs = db.relationship('Track', secondary='track_genres', back_populates='genres')

class ArtistGenre(db.Model):
    __tablename__= 'artist_genres'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class TrackGenre(db.Model):
    __tablename__= 'track_genres'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

class PlaylistTrack(db.Model):
    __tablename__= 'playlist_tracks'
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'))
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))

class TrackFeature(db.Model):
    __tablename__= 'track_features'
    id = db.Column(db.Integer, primary_key=True)
    track_id = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    feature_id = db.Column(db.Integer, db.ForeignKey('features.id'))
