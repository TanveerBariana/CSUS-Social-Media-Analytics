import login
import pandas


file1a = 'example1aresults.csv'
request = login.youtube.channels().list(
        part="snippet,contentDetails,statistics",
        forUsername= 'BaratsAndBereta'
    )
response = request.execute()
print(response['items'][0]['id'])



