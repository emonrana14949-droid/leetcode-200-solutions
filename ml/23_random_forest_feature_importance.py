# Feature Importance - most important iris feature is petal length.
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np
def run():
    X, y = load_iris(return_X_y=True)
    m = RandomForestClassifier(n_estimators=100, random_state=42).fit(X, y)
    return m.feature_importances_

if __name__ == "__main__":
    imp = run()
    assert len(imp) == 4 and abs(imp.sum() - 1.0) < 1e-9
    assert int(np.argmax(imp)) in (2, 3)
    print("ok")
