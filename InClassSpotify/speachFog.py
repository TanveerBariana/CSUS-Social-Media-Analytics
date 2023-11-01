import matplotlib.pyplot as plt
import pandas
from wordcloud import WordCloud

#Create an empty dataframe
yelp_data_in_dataframe = pandas.DataFrame()
#Put the contents of the csv file into the dataframe
yelp_data_in_dataframe = pandas.read_csv("assignment3\SongScrapeDrake.csv")

# I created a new dictionary here
yelp_review_dictionary = {}
#I am assinging the post text column data into the dictionary
yelp_review_dictionary = yelp_data_in_dataframe.get('Lyrics')

# I am converting dictionary to a list so I can analyze the data
yelp_review_list = list(yelp_review_dictionary.values)

#I am converting list to string so I can analyze the data
yelp_review_string = ''
for eachletter in  str(yelp_review_list):
    yelp_review_string += eachletter


#I am cleaning the text in reviews a bit before drawing the wordcloud
cleaned_text = yelp_review_string.replace("\\n","")
cleaned_text = yelp_review_string.replace("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});","")
cleaned_text = yelp_review_string.replace("https","")
cleaned_text = yelp_review_string.replace("\\s","")
cleaned_text = yelp_review_string.replace('\\',"")

#World cloud requires a string as input
wordcloud = WordCloud(width = 500, height = 500,
            background_color ='white',
            min_font_size = 10).generate(cleaned_text )

plt.figure(figsize = (15, 10), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

