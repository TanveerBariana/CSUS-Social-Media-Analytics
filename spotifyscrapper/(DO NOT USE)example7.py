import pandas

#Create an empty dataframe
input_data_in_dataframe = pandas.DataFrame()
#Put the contents of the csv file into the dataframe
#FYI example 3 results csv file is about Rihanna
input_data_in_dataframe = pandas.read_csv("example3results.csv")

SongNames= input_data_in_dataframe['SongName']

SongNamesList=list(SongNames)

#print(SongNamesList)

#I am now going to use this list that contains all song names of a singer to find each song's lyrics

import azapi
import time
API = azapi.AZlyrics('google', accuracy=0.5)
#Since example 3 results is about Rihanna, I keep the artist name same below. Otherwise, change the artist name accordingly
API.artist = 'Rihanna'

#print(SongNamesList)
#Clean Song Names to prevent errors when searching for lyrics

separator = ' -'
cleanedsonglist=[]
for song in SongNamesList:
 cleansong = song.split(separator, 1)[0]
 cleanedsonglist.append(cleansong)

#print(cleanedsonglist)
output={"Song":[],"Lyrics":[]}
timeCheck = 0
for song in (cleanedsonglist):
  API.title = song
  if (API.getLyrics(save=True, ext='lrc') !=''):
   print("Song:", API.title)
   print(API.lyrics)
   output["Song"].append(API.title)
   output["Lyrics"].append(API.lyrics)
   if timeCheck == 5:
    time.sleep(10)
    timeCheck = 0
  timeCheck += 1

results = pandas.DataFrame(output)
results.to_csv('example7results.csv', index=True, index_label="Index")
print("done")
