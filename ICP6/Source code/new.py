import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.cluster.vq import kmeans
from sklearn import metrics
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

data = pd.read_csv('CC.csv')
print(data.shape)
df = data.iloc[:7500, 1:]
data_notscaled = df.apply(lambda y: y.fillna(y.mean()), axis=0)

# elbow approch
distrotions = []
num_cluster = range(1, 12)
for i in num_cluster:
    centroid, distrotion = kmeans(data_notscaled, i)
    distrotions.append(distrotion)
irisplot = pd.DataFrame({'num_cluster': num_cluster, 'distrotions': distrotions})
sns.lineplot(x=irisplot.num_cluster, y=irisplot.distrotions)
plt.title("Elbow approch")
plt.show()


# defined function for knn
def clusters(dataframe):
    km = KMeans(n_clusters=2)
    km.fit(dataframe)
    # predict the cluster for each data point
    y_cluster_kmeans = km.predict(dataframe)
    # silhouette score
    score = metrics.silhouette_score(dataframe, y_cluster_kmeans)
    print('silhouette_score :', score)

    # initialising colors for the plot
    LABEL_COLOR_MAP = {0: 'r',
                       1: 'g',
                       2: 'b',
                       }

    # assigning colors to the clustered points
    label_color = [LABEL_COLOR_MAP[l] for l in km.predict(dataframe)]
    plt.figure(figsize=(8, 6))
    plt.title('K means clustering')
    plt.scatter(dataframe.iloc[:, 0], dataframe.iloc[:, 1], c=label_color)
    plt.show()

    # find the clusters with knn without scale


print("Cluster without scaled")
clusters(data_notscaled)

# scale
scaler = preprocessing.MinMaxScaler()
scaler.fit(data_notscaled)
data_scaled = scaler.transform(data_notscaled)
data_scaled = pd.DataFrame(data_scaled)
print("clusters scaled data")
clusters(data_scaled)
# Now applying PCA to scaled Data
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(data_scaled)
principalDf = pd.DataFrame(data=principalComponents, columns=['principal component 1', 'principal component 2'])
print("after applying the PCA")
clusters(principalDf)
