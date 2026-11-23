# Gaussian Naive Bayes - classify iris, accuracy above 0.9.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
def run():
    X, y = load_iris(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = GaussianNB().fit(Xtr, ytr)
    return accuracy_score(yte, m.predict(Xte))

if __name__ == "__main__":
    assert run() > 0.9
    print("ok")
