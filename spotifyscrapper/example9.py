import pandas
import time
#Create an empty dataframe
input_data_in_dataframe = pandas.DataFrame()
#Put the contents of the csv file into the dataframe
#FYI example 3 results csv file is about Rihanna
input_data_in_dataframe = pandas.read_csv("spotifyscrapper\example3results.csv")

SongNames= input_data_in_dataframe['SongName']

SongNamesList=list(SongNames)

separator = ' -'
cleanedsonglist=[]
for song in SongNamesList:
 cleansong = song.split(separator, 1)[0]
 cleanedsonglist.append(cleansong)

import lyricsgenius

#Put your access token from Genius Below 
genius = lyricsgenius.Genius('35ijaQorzfnHHqlGTMEJPVmzYfeCG8uIO_bggY0KBBG9WEdp5MyxZZ2fqOa56w1N')

artist = genius.search_artist("Rihanna", max_songs=3, sort="title", include_features=True)
#print(artist.songs)

#song = artist.song("Diamonds")
#print(song.lyrics)

output={"Song":[],"Lyrics":[]}
timeCheck = 0
for listitem in (cleanedsonglist):
    print("Song:", listitem)
    song=artist.song(listitem)
    if (song is not None):
      if(song.lyrics is not None):
       print(song.lyrics)
       output['Song'].append(song)
       #The first line in the output looks weird so I am deleting it below
       cleanedlyrics = song.lyrics.split("\n",1)[1]
       output['Lyrics'].append(cleanedlyrics)
    if timeCheck == 6:
        time.sleep(10)
        timeCheck = 0
    timeCheck += 1

results = pandas.DataFrame(output)
results.to_csv('spotifyscrapper\example9results.csv', index=True, index_label="Index")
print("done")
