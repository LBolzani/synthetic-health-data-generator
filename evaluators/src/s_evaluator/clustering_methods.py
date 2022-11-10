from sklearn.cluster import KMeans

def get_kmeans_clusters(df, n_clusters):
    kmeans = KMeans(n_clusters = n_clusters)
    kmeans.fit(df)
    k_clusters = kmeans.labels_ + 1
    return k_clusters