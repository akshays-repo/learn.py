import pandas as pd
import matplotlib.pylab as plt 
Univ = pd.read_csv("Universities.csv")

def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

df_norm = norm_func(Univ.iloc[:,1:])

from scipy.cluster.hierarchy import linkage 
import scipy.cluster.hierarchy as sch # for creating dendrogram 

print(type(df_norm))

z = linkage(df_norm, method="complete",metric="euclidean")
plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8., 
    # font size for the x axis labels
)
plt.show()

# Now applying AgglomerativeClustering choosing 3 as clusters from the dendrogram
from	sklearn.cluster	import	AgglomerativeClustering 
h_complete  = AgglomerativeClustering(n_clusters=3, linkage='complete',affinity = "euclidean").fit(df_norm) 
print(h_complete.labels_)

cluster_labels=pd.Series(h_complete.labels_)

Univ['clust']=cluster_labels # creating a  new column and assigning it to new column 
Univ = Univ.iloc[:,[7,0,1,2,3,4,5,6]]
print(Univ.head())

# getting aggregate mean of each cluster
Univ.groupby(Univ.clust).mean()

# creating a csv file 
Univ.to_csv("University.csv") #,encoding="utf-8")

from sklearn.cluster import AgglomerativeClustering 
import numpy as np 

# randomly chosen dataset 
X = np.array([[1, 2], [1, 4], [1, 0], 
			[4, 2], [4, 4], [4, 0]]) 

# here we need to mention the number of clusters 
# otherwise the result will be a single cluster 
# containing all the data 
clustering = AgglomerativeClustering(n_clusters = 2).fit(X) 

# print the class labels 
print(clustering.labels_) 
