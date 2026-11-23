# Polynomial Fit - fit y = x^2 with a degree-2 polynomial.
import numpy as np
def fit_poly(x, y):
    return np.polyfit(x, y, 2)

if __name__ == "__main__":
    x = np.array([0.0, 1.0, 2.0, 3.0])
    c = fit_poly(x, x ** 2)
    assert abs(c[0] - 1.0) < 1e-9
    print("ok")
