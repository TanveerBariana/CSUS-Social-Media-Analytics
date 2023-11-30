import pandas

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

print(caption_text_instring)

