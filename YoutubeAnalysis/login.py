from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


import os
import pickle

#This is where we declare the scope of all the youtube analytics based pages we want to build.
#This scope indicates that all the apps that will login to Yotube's Servers will only read the youtube data and will not change anything
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

#The code below logs into the Youtube's Servers by using the credentials.json library

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"
#Make sure the json file name below matches your json file which you put into your project folder
client_secrets_file = "YoutubeAnalysis\\credentials.json"
creds = None
# the file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time
if os.path.exists("token.pickle"):
 with open("token.pickle", "rb") as token:
  creds = pickle.load(token)
# if there are no (valid) credentials availablle, let the user log in.
if not creds or not creds.valid:
  if creds and creds.expired and creds.refresh_token:
     creds.refresh(Request())
  else:
     flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
     creds = flow.run_local_server(port=0)
# save the credentials for the next run
with open("token.pickle", "wb") as token:
 pickle.dump(creds, token)

youtube = build(api_service_name, api_version, credentials=creds)
