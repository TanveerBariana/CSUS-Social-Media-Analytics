import pandas

#I am creating a dictionary here titled inputdata
inputdata={}
#I am assigning the content of the csv file to my dictionary
#header is my row in the csv file that is why header is 0 below
inputdata = pandas.read_csv('spotifyscrapper\example8.py', header=[0], index_col=0).to_dict()

#We can use type to check the data type of a variable
#print(type(inputdata))

#I am using the column headers from the csv file to find the data I am interested to analyze

# I created a new dictionary here for the description column in my csv file
lyricsdictionary = inputdata.get('Lyrics')
#print(type(descriptiondictionary))

# I am converting the dictionary to a list so I can analyze the data
lyricslist =  list(lyricsdictionary.values())
#print(lyricslist)


from profanity_check import predict, predict_prob

#0 means there is no offensive language. 1 is the opposite
profanity_prediction_list = predict(lyricslist)
print(profanity_prediction_list)

profanity_probability_list= predict_prob(lyricslist)
print(profanity_probability_list)

file = pandas.read_csv('spotifyscrapper\example8.py')
file['Profanity Prediction Score'] = profanity_prediction_list
file['Profanity Prediction Probability'] = profanity_probability_list

#Index is false because example 1.csv file already has an index column
file.to_csv('spotifyscrapper\example11results.csv', index=False)

print("done")
