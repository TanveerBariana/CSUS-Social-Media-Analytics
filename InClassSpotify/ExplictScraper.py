import pandas
import re

#I am creating a dictionary here titled inputdata
inputdata={}
#I am assigning the content of the csv file to my dictionary
#header is my row in the csv file that is why header is 0 below
inputdata = pandas.read_csv('assignment3\SongScrapeDrake.csv', header=[0], index_col=0).to_dict()

#We can use type to check the data type of a variable
#print(type(inputdata))

#I am using the column headers from the csv file to find the data I am interested to analyze

# I created a new dictionary here for the description column in my csv file
lyricsdictionary = inputdata.get('Lyrics')
#print(type(descriptiondictionary))

# I am converting the dictionary to a list so I can analyze the data
lyricslist =  list(lyricsdictionary.values())

lyrics_string= str(lyricslist)
#I am cleaning the lyrics text
cleaned_text = lyrics_string.replace("\\n","")
cleaned_text = lyrics_string.replace("<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});","")
cleaned_text = lyrics_string.replace("\\s","")
cleaned_text = lyrics_string.replace('\\',"")

#Open explicit words file
explicitwords_file = open("spotifyscrapper\explicitwords.txt", "r")

explicitwords_data_string = explicitwords_file.read()

pattern = r'[0-9]'

explicitwords_data_string = re.sub(pattern, '', explicitwords_data_string)

explicitwords_list= explicitwords_data_string.split()
output={"ExplicitWords":[]}
songs_explicit_words_list=[]
for explicitword in explicitwords_list:
    counter=0
    if len(explicitword)>2:
        if (explicitword not in ['dream','play','make','hit','wild','off','men','her','your','and','love','huge','tea','one','two','are','baby','straight','gone', 'baby' 'men','brown','white','eat','black','girl','hot','jack','come','jacket']):
         if explicitword in cleaned_text:
            #print(explicitword)
            songs_explicit_words_list.append(explicitword)

output = {"ExplicitWord":[],"Frequency":[]}
counterdictionary={}
for explicitword in songs_explicit_words_list:
    output["ExplicitWord"].append(explicitword)
    counterdictionary[explicitword] = songs_explicit_words_list.count(explicitword)
    output['Frequency'].append(counterdictionary[explicitword])

# Remove duplicate values in dictionary
# Using setdefault() method

results = pandas.DataFrame(output)
results= results.drop_duplicates(keep='first')
#print(results)

#Explicit Words in Rihanna's Scraped Songs
results.to_csv('assignment3\ExplictScrapeDrake.csv', index=True, index_label="Index")
print("done")
