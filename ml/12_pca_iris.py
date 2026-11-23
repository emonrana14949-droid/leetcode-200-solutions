# PCA - reduce iris to 2 components, keep most variance.
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
def run():
    X, _ = load_iris(return_X_y=True)
    p = PCA(n_components=2, random_state=42).fit(X)
    return p.explained_variance_ratio_.sum(), p.transform(X).shape

if __name__ == "__main__":
    v, shape = run()
    assert v > 0.9 and shape == (150, 2)
    print("ok")
