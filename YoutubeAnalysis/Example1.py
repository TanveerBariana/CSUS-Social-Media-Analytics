import login
import pandas

request = login.youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername="JayzTwoCents"
    )
response = request.execute()

#print(response)
#Note the api does not display total number of likes and uploads per channel
#Response output is difficult to work with. I select outputs I like from the response and put them into a dataframe

results_dataframe= pandas.json_normalize(response['items'])[['snippet.title','snippet.description','snippet.country','statistics.viewCount','statistics.subscriberCount','statistics.videoCount']]

results_dataframe.to_csv("YoutubeAnalysis\\example1results.csv", index=False)
