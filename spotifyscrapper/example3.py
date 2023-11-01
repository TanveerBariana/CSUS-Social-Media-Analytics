import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas
#Put your App’s Client ID and Secret Below
client_id = "Your App Client ID Goes Here"
client_secret = "Your app Client Secret Goes Here"
client_credentials_manager = SpotifyClientCredentials(client_id='f7463345769f4254b3dacca8c5a40fe6', client_secret='a395a988201a42879a3c27ad432a419e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

output = {'SongName':[],"AlbumName":[]}

#You can put multiple artists below
name = ['Rihanna']
result = sp.search(name)
result['tracks']['items'][1]['artists']

# Extract Artist's uri
artists_uris = result['tracks']['items'][0]['artists'][0]['uri']
# Pull all of the artist's albums
artist_albums = sp.artist_albums(artists_uris, album_type='album')
# Store artist's albums' names' and uris in separate lists
artist_album_names = []
artist_album_uris = []
for i in range(len(artist_albums['items'])):
    artist_album_names.append(artist_albums['items'][i]['name'])
    artist_album_uris.append(artist_albums['items'][i]['uri'])

#print(artist_album_names)
#print(artist_album_uris)

# Keep names and uris in same order to keep track of duplicate albums

#Extract all the songs from every album

def album_songs(uri):
    album = uri
    spotify_albums[album] = {}
    #Create keys-values of empty lists inside nested dictionary for album
    spotify_albums[album]['album'] = []
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []
    #pull data on album tracks
    tracks = sp.album_tracks(album)

    for n in range(len(tracks['items'])):
        spotify_albums[album]['album'].append(artist_album_names[album_count])
        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
        #print(tracks['items'][n]['name'])
        output['SongName'].append(tracks['items'][n]['name'])
        #print(artist_album_names[album_count])
        output['AlbumName'].append(artist_album_names[album_count])

spotify_albums = {}
album_count = 0
for i in artist_album_uris: #each album
    album_songs(i)
    #print(str(artist_album_names[album_count]) + " album songs has been added to spotify_albums dictionary")
    album_count+=1 #Updates album count once all tracks have been added

results = pandas.DataFrame(output)
results.to_csv('spotifyscrapper\example3results.csv', index=True, index_label="Index")
print("done")
