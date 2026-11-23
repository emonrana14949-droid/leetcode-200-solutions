# Polynomial Regression - fit a curved line to y = x^2 + noise.
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import numpy as np
def run():
    rng = np.random.default_rng(42)
    X = rng.uniform(0, 3, 100).reshape(-1, 1)
    y = X.ravel() ** 2 + rng.normal(0, 0.1, 100)
    m = make_pipeline(PolynomialFeatures(2), LinearRegression()).fit(X, y)
    return r2_score(y, m.predict(X))

if __name__ == "__main__":
    assert run() > 0.95
    print("ok")
