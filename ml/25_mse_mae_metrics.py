# MSE and MAE - error of linear regression on diabetes data.
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
def run():
    X, y = load_diabetes(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = LinearRegression().fit(Xtr, ytr)
    p = m.predict(Xte)
    return mean_squared_error(yte, p), mean_absolute_error(yte, p)

if __name__ == "__main__":
    mse, mae = run()
    assert mse > 0 and mae > 0 and mae < 100
    print("ok")
