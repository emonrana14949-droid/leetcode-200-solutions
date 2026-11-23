# GridSearchCV - find the best k for KNN on iris.
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
def run():
    X, y = load_iris(return_X_y=True)
    g = GridSearchCV(KNeighborsClassifier(), {"n_neighbors": [1, 3, 5]}, cv=3).fit(X, y)
    return g.best_params_, g.best_score_

if __name__ == "__main__":
    params, score = run()
    assert params["n_neighbors"] in (1, 3, 5) and score > 0.9
    print("ok")
