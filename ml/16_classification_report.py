# Classification Report - accuracy of random forest on breast cancer.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
def run():
    X, y = load_breast_cancer(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xtr, ytr)
    return accuracy_score(yte, m.predict(Xte))

if __name__ == "__main__":
    assert run() > 0.9
    print("ok")
