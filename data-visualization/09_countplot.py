# Countplot - Pass vs Fail
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "09_countplot.png")
import seaborn as sns
import pandas as pd
df = pd.DataFrame({"result": ["pass"] * 70 + ["fail"] * 30})
plt.figure()
sns.countplot(x="result", data=df)
plt.title("Pass vs Fail")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
