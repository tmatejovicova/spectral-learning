from sklearn.cluster import KMeans

class Clustering:
    """
    Perform k-means clustering on the given nodes
    """
    def __init__(self, X, nodes_set, m, verbose):
        self.X = X
        self.nodes_set = nodes_set
        num_samples = X.shape[0]
        if num_samples < m:
            self.m = num_samples
        else:
            self.m = m
        self.verbose = verbose
        self.__cluster()

    def __cluster(self):
        kmeans = KMeans(n_clusters = self.m)
        kmeans.fit(self.X)

        centroid = kmeans.cluster_centers_
        labels = kmeans.labels_

        for node in self.nodes_set:
            h = kmeans.predict(node.x)[0]
            node.set_h(self.m, h)
