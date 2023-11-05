import pandas

#I am creating a dictionary here titled inputdata
inputdata={}
#I am assigning the content of the csv file to my dictionary
#header is my row in the csv file that is why header is 0 below
inputdata = pandas.read_csv('assignment3\ArtistScrapeDrake3.csv', header=[0], index_col=0).to_dict()

#We can use type to check the data type of a variable
#print(type(inputdata))

#I am using the column headers from the csv file to find the data I am interested to analyze

# I created a new dictionary here for the energy column in my csv file
energydictionary = inputdata.get('energy')

# I am converting the dictionary to a list so I can analyze the data
energylist =  list(energydictionary.values())

popularitydictionary = inputdata.get('popularity')

popularitylist =  list(popularitydictionary.values())

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(energylist,popularitylist)
plt.xlabel("Energy")
plt.ylabel("Popularity")
plt.show()
