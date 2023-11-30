import os
import pandas

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = 'AIzaSyDRHh6CLEzLo7_1Mdr0ZUWLfRYT59crHeI'
    youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=100,
        videoId='bn1-M5Ze0p8'
    )
    response = request.execute()
    #print(response)
    # I am creating an empty dictionary here for the results I like to save to a CSV file
    output = {"CommentID": [], "UserID": [], "Comment": [], "Number_of_Likes": [], "Number_of_Replies": [],
              "Updated_At": []}
    results_out = pandas.DataFrame(columns=['CommentID,UserID,Comment,Number_of_Likes,Number_of_Replies,Updated_At'])
    for item in response['items']:
        # I am accessing different parts of the JSON response file that I consider important
        comment_id = item['snippet']['topLevelComment']['id']
        userID = item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
        reply_count = item['snippet']['totalReplyCount']
        updated_at = item["snippet"]["topLevelComment"]["snippet"]["updatedAt"]
        # I am appending the results for each comment
        output['CommentID'].append(comment_id)
        output['UserID'].append(userID)
        output['Comment'].append(comment)
        output['Number_of_Likes'].append(like_count)
        output['Number_of_Replies'].append(reply_count)
        output['Updated_At'].append(updated_at)

        results_in = pandas.DataFrame.from_dict(output, orient='index').T
        results_out = pandas.concat([results_out,results_in]).drop_duplicates()
    print("Done, file",'example5results.csv','is ready.')
    results_out.to_csv('YoutubeAnalysis\\example5results.csv', index=False)
       
if __name__ == "__main__":
    main()
