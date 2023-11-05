import pandas

#I am creating a dictionary here titled inputdata
inputdata={}
#I am assigning the content of the csv file to my dictionary
#header is my row in the csv file that is why header is 0 below
inputdata = pandas.read_csv('assignment3\ArtistScrapeDrake2.csv', header=[0], index_col=0).to_dict()

#We can use type to check the data type of a variable
#print(type(inputdata))

#I am using the column headers from the csv file to find the data I am interested to analyze

# I created a new dictionary here for the description column in my csv file
songdictionary = inputdata.get('name')

# I am converting the dictionary to a list so I can analyze the data
songlist =  list(songdictionary.values())

danceabilitydictionary = inputdata.get('tempo')

danceabilitylist =  list(danceabilitydictionary.values())

import matplotlib.pyplot as plt

x_axis = songlist
y_axis = danceabilitylist

plt.plot(x_axis, y_axis)
plt.title('Danceability Trend')
plt.xlabel('Danceability')
plt.ylabel('Songs')
plt.show()
