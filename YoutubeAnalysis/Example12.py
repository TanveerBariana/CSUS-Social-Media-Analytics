from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas
import numpy

#I am creating a dictionary here titled inputdata
inputdata={}

inputdata = pandas.read_csv('YoutubeAnalysis\\example10_results.csv').to_dict()

# I created a new dictionary here for the comment column in my csv file

readability_dictionary = inputdata.get('Readability')

sarcasm_dictionary = inputdata.get("Is_Sarcastic")

readability_list =  list(readability_dictionary.values())

sarcasm_list =  list(sarcasm_dictionary.values())

updated_sarcasm_list = []
for i in sarcasm_list:
    if i == 'Not Sarcasm':
        updated_sarcasm_list.append(int('0'))
    elif i =='Sarcasm':
        updated_sarcasm_list.append(int('1'))

combined_list = list(zip(readability_list,updated_sarcasm_list))

from sklearn.preprocessing import normalize
data_scaled = normalize(combined_list)

import scipy.cluster.hierarchy as shc
plt.figure(figsize=(10, 7))
plt.title("Dendrograms")
dend = shc.dendrogram(shc.linkage(data_scaled, method='ward'))
plt.show()

from sklearn.cluster import AgglomerativeClustering

#Based on the dendogram, there are 2 clusters. Below, we can find each cluster each readability score belongs to
#Change number 2 below based on your interpretation of the dendogram
cluster = AgglomerativeClustering(
    n_clusters=2, affinity='euclidean', linkage='ward')

cluster.fit(data_scaled)
labels = cluster.labels_
labels
print(labels)
