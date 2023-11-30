import login
import pandas


appended_data_list = []
while True:
    userinput = input("Enter Youtube Channel ID: ")
    # your code

    request = login.youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=userinput
    )
    response = request.execute()


    # print(response)
    # Note the api does not display total number of likes and uploads per channel
    # Response output is difficult to work with. I select outputs I like from the response and put them into a dataframe

    results_dataframe = pandas.json_normalize(response['items'])[
        ['snippet.title', 'snippet.description', 'snippet.country', 'statistics.viewCount',
         'statistics.subscriberCount', 'statistics.videoCount']]

    appended_data_list.append(results_dataframe)

    cont = input("Another one? yes/no > ")

    while cont.lower() not in ("yes", "no"):
        cont = input("Another one? yes/no > ")

    if cont == "no":
        print("Break")
        appended_data_dataframe = pandas.concat(appended_data_list)
        appended_data_dataframe.to_csv("YoutubeAnalysis\\example2results.csv", index=False)
        break
