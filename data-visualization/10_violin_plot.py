# Violin Plot - Score Distribution
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "10_violin_plot.png")
import seaborn as sns
rng = np.random.default_rng(3)
import pandas as pd
df = pd.DataFrame({"cls": ["A"] * 50 + ["B"] * 50, "score": list(rng.normal(70, 8, 50)) + list(rng.normal(80, 8, 50))})
plt.figure()
sns.violinplot(x="cls", y="score", data=df)
plt.title("Score Distribution")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
