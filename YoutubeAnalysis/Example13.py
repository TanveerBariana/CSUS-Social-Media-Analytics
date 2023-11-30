import pandas
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#I am creating a dictionary here titled inputdata
inputdata={}

inputdata = pandas.read_csv('YoutubeAnalysis\\example11_results.csv').to_dict()

comment_dictionary = inputdata.get('Comment')

sarcasm_dictionary = inputdata.get("Is_Sarcastic")

# I am converting the comment dictionary to a list so I can analyze the data

comment_list =  list(comment_dictionary.values())

#I would like to filter comments based on sarcasm values from the csv file. Therefore, I created this sarcasm list, which I will use below
sarcasm_list = list(sarcasm_dictionary.values())

#I like to put all sarcastic comments inside the sarcastic comment list
sarcastic_comment_list = []
#I like to put ll unsarcastic comments inside the unsarcastic comment list
unsarcastic_comment_list =[]

for i in range(len(comment_list)):
    #I am using an if statement to check a row's sarcasm column value from the csv file
     if sarcasm_list[i] == 'Sarcasm':
         sarcastic_comment_list.append((comment_list[i]))
     elif sarcasm_list[i] == 'Not Sarcasm':
         unsarcastic_comment_list.append((comment_list[i]))

#I will now clean text in sarcastic comments

for i in range(len(sarcastic_comment_list)):
    # I am cleaning the comments data
    # 1. make all letters lowercase
    sarcastic_comment_list[i] = sarcastic_comment_list[i].lower()
    # 2. Remove special characters
    sarcastic_comment_list[i] = re.sub(r'\W+', ' ', sarcastic_comment_list[i])
    # 3. Remove numbers
    sarcastic_comment_list[i] = ''.join(c if c not in map(str, range(0, 10)) else "" for c in sarcastic_comment_list[i])
    # 4. Remove stop words
    # We need to convert the string to tokens in order to remove the stop words then convert the tokens back to string format
    # A token is a string of contiguous characters between two spaces, or between a space and punctuation marks.
    sarcastic_comment_tokens = word_tokenize(sarcastic_comment_list[i])

    cleaned_sarcastic_comment_tokens = [word for word in sarcastic_comment_tokens if not word in stopwords.words()]

    # I am converying the tokens back into string as an input for the wordcloud. Wordcloud does not accept token as input
    cleaned_sarcastic_comments_string_data = TreebankWordDetokenizer().detokenize(cleaned_sarcastic_comment_tokens)


#I am drawing a wordcloud for the sarcastic comments
wordcloud = WordCloud(width=500, height=500,
                          background_color='white',
                          min_font_size=10).generate(cleaned_sarcastic_comments_string_data)

plt.figure(figsize=(15, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.title("Sarcastic Comments WordCloud")
plt.show()
