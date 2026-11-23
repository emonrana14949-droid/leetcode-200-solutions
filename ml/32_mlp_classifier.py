# MLP Classifier - a small neural network on iris.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
def run():
    X, y = load_iris(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = make_pipeline(StandardScaler(), MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)).fit(Xtr, ytr)
    return accuracy_score(yte, m.predict(Xte))

if __name__ == "__main__":
    assert run() > 0.85
    print("ok")
