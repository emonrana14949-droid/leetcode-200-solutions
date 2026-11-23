# Pairplot - Iris Features
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "28_pairplot.png")
import seaborn as sns
df = sns.load_dataset("iris")
g = sns.pairplot(df, hue="species")
g.savefig(PATH)
plt.close("all")

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
