# K-Means Elbow - inertia falls as k grows.
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
def run():
    X, _ = load_iris(return_X_y=True)
    return [KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_ for k in [2, 3, 4]]

if __name__ == "__main__":
    vals = run()
    assert vals[0] > vals[1] > vals[2]
    print("ok")
