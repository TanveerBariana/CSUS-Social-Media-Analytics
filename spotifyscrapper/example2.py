import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas

#Put your App’s Client ID and Secret Below
client_credentials_manager = SpotifyClientCredentials(client_id='f7463345769f4254b3dacca8c5a40fe6', client_secret='a395a988201a42879a3c27ad432a419e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#I am creating an empty dictionary here
output = {"ArtistName":[],"ArtistPopularity":[],"ArtistGenres":[],"SongName":[],'SongPopularity':[],'AlbumName':[]}


playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=77d8f5cd51cd478d&nd=1"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    # URI
    track_uri = track["track"]["uri"]

    # Track name
    track_name = track["track"]["name"]
    #print(track_name)
    output['SongName'].append(track_name)

    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    # Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    output['ArtistPopularity'].append(artist_pop )
    artist_genres = artist_info["genres"]
    #print(artist_genres)
    output['ArtistGenres'].append(artist_genres)
    #print(artist_name)
    output['ArtistName'].append(artist_name)
    #print(artist_pop)

    # Album
    album = track["track"]["album"]["name"]
    #print(album)
    output['AlbumName'].append(album)

    # Popularity of the track
    track_pop = track["track"]["popularity"]
    # print(track_pop)
    output['SongPopularity'].append(track_pop )

results = pandas.DataFrame(output)
results.to_csv('spotifyscrapper\example2results.csv', index=True, index_label="Index")
print("done")
