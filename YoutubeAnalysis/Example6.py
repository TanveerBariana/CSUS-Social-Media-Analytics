from youtube_transcript_api import YouTubeTranscriptApi
import pandas

# assigning srt variable with the list
# of dictonaries obtained by the get_transcript() function
caption_list = YouTubeTranscriptApi.get_transcript("6eH2BItdo0M")
#print(caption_list)

caption_dataframe = pandas.DataFrame(caption_list)

caption_dataframe.to_csv("YoutubeAnalysis\\example6results.csv", index=False)
