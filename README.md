# Visualization & Evaluation of Artists and Tracks on Spotify

## Project Motivation
The purpose of this project was to understand the characteristics of artists and tracks that are representative of their genres. 

## ETL
Due to the nature of the Spotify API (artist/album/track IDs must be specified in order to retrieve associated data), 8 artists from diverse genres were selected:

* Pop: Charlie Puth, Michael Jackson
* Hip-Hop: Migos, Biggie Smalls
* Rock: Fall-Out Boy, Aerosmith
* Country: Carrie Underwood, Sheryl Crow
* Dance/EDM: Bee-Gees, Marshmello

For each genre, two artists were selected: a modern artist and a past artist. These artists may be considered representative of their respective genre for the time period.

## Spotify Features
[Spotify](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/) has an algorithm which determines the values for different track features. The following features were used:

* Danceability
* Energy
* Acousticness
* Valence
* Tempo

## SQL Database Schema
SQLAlchemy was used to construct the schema for the SQL database. 

## Dashboard
A dashboard, with Dash as the front-end and Flask as the back-end, was built to display visualizations. 

## Top Songs vs. Other Songs
Top songs were defined using Spotify's algorithm (based on number of all-time streams and recent streams). Other songs were taken from the artist's select albums. 

### Average Feature Values by Artist
For a given artist, the average feature value was calculated by averaging the feature values across all their sampled songs. For example, the danceability values were taken from all of Michael Jackson's sampled songs and averaged to produce the average danceability value for Michael Jackson. This allows us to compare the average values across artists. 

![header](images/avg_features.png)

Of note, Migos was considered more danceable on average, compared to Michael Jackson. 

### Select Artist Track Visualization by Feature(s) 
For a given artist, the distribution of feature values can be compared for top songs vs. other songs. 

![header](images/artist_track_features.png)

### Intra-Genre Generational Differences
Intra-genre comparisons can be made, comparing an older-generation artist to a modern-day artist. This allows us to understand if there are any distinct differences across generations. The selected artists are/were popular artists that representative of the genre for their time. Any generational differences may speak to differences in generational preferences in sound. 

![header](images/edm_dance_comp.png)

![header](images/hip_hop_comp.png)

![header](images/pop_comp.png)

Overall, it's notable that older artists were generally more 'positive' than their modern-day counterparts. This may even reflect generational mood, given current events. 

### Distribution of All Top Tracks by Feature
Across all top tracks, what are the distributions for each feature? 

![header](images/feature_dist.png)

If top tracks varied greatly in feature values, we would expect wider distributions. However, it's evident that all top tracks, regardless of genre, seem to be more 'danceable' and energetic. This may reflect public preferences in mainstream music, irrespective of the genre. The public may generally prefer songs that are more danceable and energetic. 

### Artist Feature Comparisons 
The feature values for different artists could be compared. 
![header](images/artist_comp.png)


