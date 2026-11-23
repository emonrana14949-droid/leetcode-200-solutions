# Cross-Validation - 5-fold score of logistic regression on iris.
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
def run():
    X, y = load_iris(return_X_y=True)
    return cross_val_score(LogisticRegression(max_iter=1000), X, y, cv=5).mean()

if __name__ == "__main__":
    assert run() > 0.9
    print("ok")
