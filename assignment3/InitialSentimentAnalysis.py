import pandas
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv

#I am creating a dictionary here titled inputdata
inputdata={}
#I am assigning the content of the csv file to my dictionary
#header is my row in the csv file that is why header is 0 below
inputdata = pandas.read_csv('assignment3\SongScrapeAlbum3.csv', header=[0]).to_dict()

#We can use type to check the data type of a variable
#print(type(inputdata))

#I am using the column headers from the csv file to find the data I am interested to analyze

# I created a new dictionary here for the description column in my csv file
descriptiondictionary = inputdata.get('Lyrics')
#I am converting the decription from dictionary to a list for the sentiment analyses below
descriptionlist =  list(descriptiondictionary.values())

textblob_results_list=[]
vader_results_list=[]

for i in range(len(descriptionlist )):
    #This is TextBlob Based Sentiment Analysis
    textblob_analyze_polarity = TextBlob(descriptionlist [i]).polarity
    textblob_analyze_subjectivity = TextBlob(descriptionlist [i]).subjectivity
    #polarity values range from -1 to 1 where -1.0 is negative polarity and 1.0 is positive
    #Subjectivity/objectivity  values range from 0.0 to 1.0 where 0.0 is very objective and 1.0 is very subjective
    #print("Polarity: ", textblob_analyze_polarity)
    #print("Subjectivity: ",textblob_analyze_subjectivity)

    textblob_result = {"TextBlob Polarity Score":textblob_analyze_polarity,"TextBlob Subjectivity Score": textblob_analyze_subjectivity}
    textblob_results_list.append(textblob_result)

    #This is Vader Based Sentiment Analysis
    #Vader provides 4 results labeled as negative, neutral, positive, and compound(overall)
    vader_sentiment_analysis = SentimentIntensityAnalyzer().polarity_scores(descriptionlist [i])
    vader_results_list.append(vader_sentiment_analysis)
    #In Vader the compound score is the sum of positive, negative, and neutral scores which is then
    #normalized between -1 [most extreme negative] and 1[most extreme positive]
    #negative represents negative aspects of a tweet
    #positive represents positive aspects of a tweet
    #neutral represents neutral aspects of a tweet
    #print("Polarity Scores in Vader: ", vader_sentiment_analysis)

#This is the TextBlob Sentiment Analysis Results
textblobresults = pandas.DataFrame(textblob_results_list)

#This is the Vader Sentiment Analysis Results
vaderresults = pandas.DataFrame(vader_results_list)
#print(textblobresults['TextBlob Polarity Score'])
#print(vaderresults['neg'])

file = pandas.read_csv('assignment3\SongScrapeAlbum3.csv')
file['TextBlob Polarity Score'] = textblobresults['TextBlob Polarity Score']
file['TextBlob Subjectivity Score'] = textblobresults['TextBlob Subjectivity Score']
file['Vader Negative Polarity Score'] = vaderresults['neg']
file['Vader Neutral Polarity Score'] = vaderresults['neu']
file['Vader Positive Polarity Score'] = vaderresults['pos']
file['Vader Compound Polarity Score'] = vaderresults['compound']

#Index is false because example 1.csv file already has an index column
file.to_csv('assignment3\SentimentAlbum3.csv', index=True, index_label="Index")

print("done")

