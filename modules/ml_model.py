from sklearn.cluster import KMeans

def train_model(features):
    model = KMeans(n_clusters=3)
    model.fit(features)
    return model