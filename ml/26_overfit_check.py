# Overfitting Check - a deep tree fits train better than test.
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
def run():
    X, y = load_diabetes(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = DecisionTreeRegressor(random_state=42).fit(Xtr, ytr)
    return r2_score(ytr, m.predict(Xtr)), r2_score(yte, m.predict(Xte))

if __name__ == "__main__":
    tr, te = run()
    assert tr > te
    print("ok")
