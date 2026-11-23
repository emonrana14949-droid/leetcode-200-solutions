# Confusion Matrix - 3x3 matrix for iris predictions.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
def run():
    X, y = load_iris(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
    return confusion_matrix(yte, m.predict(Xte))

if __name__ == "__main__":
    cm = run()
    assert cm.shape == (3, 3) and cm.sum() == 30
    print("ok")
