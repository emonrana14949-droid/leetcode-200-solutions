# K-Means - cluster iris into 3 groups, check we get 3 clusters.
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
def run():
    X, _ = load_iris(return_X_y=True)
    m = KMeans(n_clusters=3, n_init=10, random_state=42).fit(X)
    return len(set(m.labels_))

if __name__ == "__main__":
    assert run() == 3
    print("ok")
