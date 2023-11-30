import pandas
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# This is the training data with already categorized messages
data = pandas.read_json("YoutubeAnalysis\Sarcasm_Headlines_Dataset.json", lines=True)
#print(data.head())

data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
#print(data.head())

data = data[["headline", "is_sarcastic"]]
x = np.array(data["headline"])
y = np.array(data["is_sarcastic"])

cv = CountVectorizer()
X = cv.fit_transform(x) # Fit the Data
#test_size is the number that defines the size of the test set. It's very similar to train_size .
#Random stats will decide the splitting of data into train and test indices
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = BernoulliNB()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

#I am creating a dictionary here titled inputdata
inputdata={}

inputdata = pandas.read_csv('YoutubeAnalysis\example6results.csv').to_dict()

# I created a new dictionary here for the text column in my csv file

caption_text_dictionary = inputdata.get('text')

# I am converting the caption dictionary to a list so I can analyze the data

caption_text_list =  list(caption_text_dictionary.values())

#convert list to string
caption_text_instring = ''
for eachletter in  caption_text_list:
    caption_text_instring += eachletter

#I am cleaning the caption data
#1. make all letters lowercase
caption_text_instring = caption_text_instring.lower()
#2. Remove special characters
caption_text_instring = re.sub(r'\W+', ' ', caption_text_instring)
#3. Remove numbers
caption_text_instring_no_numbers = ''.join(c if c not in map(str,range(0,10)) else "" for c in caption_text_instring)

# 4. Remove stop words
#We need to convert the string to tokens in order to remove the stop words then convert the tokens back to string format
#A token is a string of contiguous characters between two spaces, or between a space and punctuation marks.
caption_tokens = word_tokenize(caption_text_instring_no_numbers)

cleaned_caption_tokens = [word for word in caption_tokens if not word in stopwords.words()]

input_data = TreebankWordDetokenizer().detokenize(cleaned_caption_tokens)

#Enter cleaned caption data to the model to check sarcasm

data = cv.transform([input_data]).toarray()
output = model.predict(data)
print(output)

# This seperator helps me to print the result without brackets and quotes
separator = ", "
print(separator.join(output))
