import pandas
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

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

inputdata = pandas.read_csv('YoutubeAnalysis\example5results.csv').to_dict()

# I created a new dictionary here for the comment column in my csv file

comment_dictionary = inputdata.get('Comment')

# I am converting the comment dictionary to a list so I can analyze the data

comment_list =  list(comment_dictionary.values())

sarcasm_results_list=[]

for i in range(len(comment_list)):
    # I am cleaning the comments data
    # 1. make all letters lowercase
    comment_list[i] = comment_list[i].lower()
    # 2. Remove special characters
    comment_list[i] = re.sub(r'\W+', ' ', comment_list[i])
    # 3. Remove numbers
    comment_list[i] = ''.join(c if c not in map(str, range(0, 10)) else "" for c in comment_list[i])
    # 4. Remove stop words
    # We need to convert the string to tokens in order to remove the stop words then convert the tokens back to string format
    # A token is a string of contiguous characters between two spaces, or between a space and punctuation marks.
    comment_tokens = word_tokenize(comment_list[i])

    cleaned_comment_tokens = [word for word in comment_tokens if not word in stopwords.words()]

    #I am converying the tokens back into string as an input for the sarcasm detector
    input_data = TreebankWordDetokenizer().detokenize(cleaned_comment_tokens)
    data = cv.transform([comment_list[i]]).toarray()
    output = model.predict(data)
    #print(output)

    #This seperator helps me to print the results without brackets and quotes
    separator = ", "
    sarcasm_result = {"Is_Sarcastic":separator.join(output) }
    sarcasm_results_list.append(sarcasm_result)

#This is the Sarcasm Analysis Results in Dataframe
sarcasm_results_dataframe = pandas.DataFrame(sarcasm_results_list)

file = pandas.read_csv('YoutubeAnalysis\\example5results.csv')
file['Is_Sarcastic'] = sarcasm_results_dataframe
file.to_csv('YoutubeAnalysis\\example9_results.csv', index=True)
