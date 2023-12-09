import pandas as pd
import statistics

df_1 = pd.read_csv('YoutubeFinal\Sentiment1.csv', header=[0])
df_2 = pd.read_csv('YoutubeFinal\Sentiment2.csv', header=[0])
df_3 = pd.read_csv('YoutubeFinal\Sentiment3.csv', header=[0])
df_4 = pd.read_csv('YoutubeFinal\Sentiment4.csv', header=[0])

TextBlob_Drink = statistics.mean([df_1['TextBlob Polarity Score'][0], df_3['TextBlob Polarity Score'][0]])
TextBlob_Angry = statistics.mean([df_2['TextBlob Polarity Score'][0], df_4['TextBlob Polarity Score'][0]])
Vader_Drink = statistics.mean([df_1['Vader Compound Polarity Score'][0], df_3['Vader Compound Polarity Score'][0]])
Vader_Angry = statistics.mean([df_2['Vader Compound Polarity Score'][0], df_4['Vader Compound Polarity Score'][0]])
Subjective_Drink = statistics.mean([df_1['TextBlob Subjectivity Score'][0], df_3['TextBlob Subjectivity Score'][0]])
Subjective_Angry = statistics.mean([df_2['TextBlob Subjectivity Score'][0], df_4['TextBlob Subjectivity Score'][0]])
TextBlob_1 = statistics.mean([df_1['TextBlob Polarity Score'][0], df_2['TextBlob Polarity Score'][0]])
TextBlob_2 = statistics.mean([df_3['TextBlob Polarity Score'][0], df_4['TextBlob Polarity Score'][0]])
Vader_1 = statistics.mean([df_1['Vader Compound Polarity Score'][0], df_2['Vader Compound Polarity Score'][0]])
Vader_2 = statistics.mean([df_3['Vader Compound Polarity Score'][0], df_4['Vader Compound Polarity Score'][0]])
Subjective_1 = statistics.mean([df_1['TextBlob Subjectivity Score'][0], df_2['TextBlob Subjectivity Score'][0]])
Subjective_2 = statistics.mean([df_3['TextBlob Subjectivity Score'][0], df_4['TextBlob Subjectivity Score'][0]])

print(" ")
print('Avg TexBlob and Vader Polarity Score for The Critical Drinker: \n'+ str(TextBlob_Drink)+ "     "+ str(Vader_Drink))
print('Avg TexBlob and Vader Polarity Score for AngryJoeShow: \n'+ str(TextBlob_Angry)+ "     "+ str(Vader_Angry))
print(" ")
print('Avg Subjectivity Score for The Critical Drinker: \n'+ str(Subjective_Drink))
print('Avg Subjectivity Score for AngryJoeShow: \n'+ str(Subjective_Angry))
print(" ")
print('Avg TexBlob and Vader Polarity Score for Season 1: \n'+ str(TextBlob_1)+ "     "+ str(Vader_1))
print('Avg TexBlob and Vader Polarity Score for Season 2: \n'+ str(TextBlob_2)+ "     "+ str(Vader_2))
print(" ")
print('Avg Subjectivity Score for Season 1: \n'+ str(Subjective_1))
print('Avg Subjectivity Score for Season2: \n'+ str(Subjective_2))
print(" ")