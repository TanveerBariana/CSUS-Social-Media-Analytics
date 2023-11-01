import spotipy
import pandas
sp = spotipy.Spotify()

#I am creating an empty dictionary here
output = {"AlbumName":[]}

#in order to gain accesss to spotify API we needed to authorise client
from spotipy.oauth2 import SpotifyClientCredentials

#Put your own client id and secret below
client_credentials_manager = SpotifyClientCredentials(client_id='f7463345769f4254b3dacca8c5a40fe6', client_secret='a395a988201a42879a3c27ad432a419e')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#creates a list of all of Rihanna's albums
#https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H
rihanna = '5pKCCKE2ajJHZ9KAiaK11H'

results = sp.artist_albums(rihanna, album_type = 'album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
       print(album['name'])
       output['AlbumName'].append(album['name'])

results = pandas.DataFrame(output)
results.to_csv('spotifyscrapper\example1results.csv', index=True, index_label="Index")
print("done")
