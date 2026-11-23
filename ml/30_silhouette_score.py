# Silhouette Score - how well K-Means clusters iris (above 0.4).
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
def run():
    X, _ = load_iris(return_X_y=True)
    labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)
    return silhouette_score(X, labels)

if __name__ == "__main__":
    assert run() > 0.4
    print("ok")
