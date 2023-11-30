import login
import pandas

request = login.youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id="bISWIk5pUH0,tWbjy_sCbUA,p79H_XOwpZo,CmNMfRpjknA"
)

response = request.execute()

#print(response)

results_dataframe= pandas.json_normalize(response['items'])[['snippet.channelTitle','snippet.title','statistics.viewCount','statistics.likeCount','statistics.commentCount', 'statistics.favoriteCount']]

#The code below renames the column names in the dataframe

results_dataframe.rename(columns= {'snippet.channelTitle': 'Channel_Title','snippet.title': 'Video_Title', 'statistics.viewCount': 'View_Count', 'statistics.likeCount':'Like_Count','statistics.commentCount':'Comment_Count','statistics.favoriteCount':'Favorite_Count'}, inplace=True)

results_dataframe.to_csv("YoutubeAnalysis\\example4results.csv", index=False)

