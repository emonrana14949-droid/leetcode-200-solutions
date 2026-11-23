# Lasso Regression - linear regression with L1 penalty.
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
def run():
    X, y = load_diabetes(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = Lasso(alpha=0.1, max_iter=5000).fit(Xtr, ytr)
    return r2_score(yte, m.predict(Xte))

if __name__ == "__main__":
    assert run() > 0.2
    print("ok")
