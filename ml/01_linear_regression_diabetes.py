# Linear Regression - predict diabetes progression, R2 should be above 0.3.
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
def run():
    X, y = load_diabetes(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = LinearRegression().fit(Xtr, ytr)
    return r2_score(yte, m.predict(Xte))

if __name__ == "__main__":
    r2 = run()
    assert r2 > 0.3, r2
    print("R2:", round(r2, 3))
    print("ok")
