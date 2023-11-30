import login
import pandas

request = login.youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id="bISWIk5pUH0"
)
response = request.execute()

print(response)

results_dataframe= pandas.json_normalize(response['items'])[['snippet.channelTitle','snippet.title','statistics.viewCount','statistics.likeCount','statistics.commentCount', 'statistics.favoriteCount']]

results_dataframe.to_csv("YoutubeAnalysis\\example3results.csv", index=False)
