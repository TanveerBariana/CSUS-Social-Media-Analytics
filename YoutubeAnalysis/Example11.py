from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
import pandas

#I am creating a dictionary here titled inputdata
inputdata={}

inputdata = pandas.read_csv('YoutubeAnalysis\\example10_results.csv').to_dict()

# I created a new dictionary here for the comment column in my csv file

readability_dictionary = inputdata.get('Readability')

readability_list =  list(readability_dictionary.values())

#Lets create a dendrogram variable
# linkage is actually the algorithm itself of hierarchical clustering and then in
#linkage we have to specify on which data we apply and engage. This is X dataset
X = [[i] for i in readability_list]

Z = linkage(X, 'ward')
fig = plt.figure(figsize=(25, 10))
dn = dendrogram(Z)
plt.title("Dendogram")
plt.xlabel('Readability Scores')
plt.ylabel('Euclidean distances')
plt.show()

from sklearn.cluster import AgglomerativeClustering

#Based on the dendogram, there are 4 clusters. Below, we can find each cluster each readability score belongs to
#Change number 4 below based on your interpretation of the dendogram
cluster = AgglomerativeClustering(
    n_clusters=4, affinity='euclidean', linkage='ward')

cluster.fit(X)
labels = cluster.labels_
#labels
#print the labels to check the cluster each message belongs to
#print(labels)

#This is the Cluster Analysis Results in Dataframe
clusteranalysis_results_dataframe = pandas.DataFrame(labels)

file = pandas.read_csv('YoutubeAnalysis\\example10_results.csv')
file['Readability_Cluster'] = clusteranalysis_results_dataframe
file.to_csv('YoutubeAnalysis\\example11_results.csv', index=True)
