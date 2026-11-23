# Train/Test Split - stratified split keeps class ratios.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
def run():
    X, y = load_iris(return_X_y=True)
    _, _, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    return np.bincount(ytr), np.bincount(yte)

if __name__ == "__main__":
    tr, te = run()
    assert tr.tolist() == [40, 40, 40] and te.tolist() == [10, 10, 10]
    print("ok")
