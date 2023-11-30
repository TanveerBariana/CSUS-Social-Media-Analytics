import pandas
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
import textstat


#I am creating a dictionary here titled inputdata
inputdata={}

inputdata = pandas.read_csv('YoutubeAnalysis\\example9_results.csv').to_dict()

# I created a new dictionary here for the comment column in my csv file

comment_dictionary = inputdata.get('Comment')

# I am converting the comment dictionary to a list so I can analyze the data

comment_list =  list(comment_dictionary.values())

readability_results_list=[]

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

    # I am converying the tokens back into string as an input for the readability detector
    input_data = TreebankWordDetokenizer().detokenize(cleaned_comment_tokens)

    readability_result = textstat.flesch_reading_ease(input_data)
    readability_results_list.append(readability_result)
    #Test the results
    #print(readability)
    #Save the results to a csv file

#This is the Readability Analysis Results in Dataframe
readability_results_dataframe = pandas.DataFrame(readability_results_list)

file = pandas.read_csv('YoutubeAnalysis\\example9_results.csv')
file['Readability'] = readability_results_dataframe
file.to_csv('YoutubeAnalysis\\example10_results.csv', index=True)
