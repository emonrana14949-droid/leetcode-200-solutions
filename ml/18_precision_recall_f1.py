# Precision / Recall / F1 - scores for breast cancer prediction.
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import precision_score, recall_score, f1_score
def run():
    X, y = load_breast_cancer(return_X_y=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    m = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
    p = m.predict(Xte)
    return precision_score(yte, p), recall_score(yte, p), f1_score(yte, p)

if __name__ == "__main__":
    pr, rc, f1 = run()
    assert pr > 0.9 and rc > 0.9 and f1 > 0.9
    print("ok")
