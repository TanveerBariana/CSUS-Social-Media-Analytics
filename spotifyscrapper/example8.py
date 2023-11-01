import lyricsgenius
import pandas
#Put your access token from Genius Below 
genius = lyricsgenius.Genius('35ijaQorzfnHHqlGTMEJPVmzYfeCG8uIO_bggY0KBBG9WEdp5MyxZZ2fqOa56w1N')

artist = genius.search_artist("Rihanna", max_songs=3, sort="title", include_features=True)
#print(artist.songs)

#song = artist.song("Diamonds")
#print(song.lyrics)

output={"Song":[],"Lyrics":[]}

songslist=['Work','Diamonds','The Monster','Wild Thoughts']

for listitem in (songslist):
    print("Song:", listitem)
    song=artist.song(listitem)
    if (song!=''):
     print(song.lyrics)
     output['Song'].append(song)
     #The first line in the output looks weird so I am deleting it below
     cleanedlyrics = song.lyrics.split("\n",1)[1]
     output['Lyrics'].append(cleanedlyrics)

results = pandas.DataFrame(output)
results.to_csv('spotifyscrapper\example8results.csv', index=True, index_label="Index")
print("done")
