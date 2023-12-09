from youtube_transcript_api import YouTubeTranscriptApi
import pandas

# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
caption_list = YouTubeTranscriptApi.get_transcript("d945RVVYeyY")
#print(caption_list)
# vid id list: IecVgTAzaRM, V_m7-mV3w90, 5aYMYhHPw1s, d945RVVYeyY
#The Critical Drinker(UCSJPFQdZwrOutnmSFYtbstA), AngryJoeShow(UCsgv2QHkT2ljEixyulzOnUQ)

caption_dataframe = pandas.DataFrame(caption_list)


inputdata = caption_dataframe.to_dict()

# I created a new dictionary here for the text column in my csv file

caption_text_dictionary = inputdata.get('text')

# I am converting the caption dictionary to a list so I can analyze the data

caption_text_list =  list(caption_text_dictionary.values())

#convert list to string
caption_text_instring = ''
for eachletter in  caption_text_list:
    caption_text_instring += eachletter
    caption_text_instring += ' '

#print(caption_text_instring)
caption_df = pandas.DataFrame()
caption_df['text'] = [caption_text_instring]
caption_df.to_csv("YoutubeFinal\\Caption4.csv", index=False)
#caption_dataframe.to_csv("YoutubeFinal\\Caption4.csv", index=False)
