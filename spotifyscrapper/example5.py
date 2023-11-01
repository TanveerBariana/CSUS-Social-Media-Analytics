import azapi

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Doja Cat'
API.title = 'Paint The Town Red'

API.getLyrics(save=True, ext='csv')

print(API.title, API.artist)
print(API.lyrics)
