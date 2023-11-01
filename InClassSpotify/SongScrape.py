import azapi
import pandas

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Drake'
songlist = ['Laugh Now Cry Later', 'One Dance', 'God\'s Plan']

output={"Song":[],"Lyrics":[]}

for song in songlist:
 API.title = song
 print("Song:",API.title,"Singer:",API.artist)
 output['Song'].append(API.title)
 API.getLyrics(save=False, ext='lrc')
 print(API.lyrics)
 output['Lyrics'].append(API.lyrics)

results = pandas.DataFrame(output)
results.to_csv('assignment3\SongScrapeDrake.csv', index=True, index_label="Index")
print("done")
