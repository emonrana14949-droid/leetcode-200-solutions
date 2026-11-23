# Scatter with Hue - Iris
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "33_scatter_hue.png")
import seaborn as sns
df = sns.load_dataset("iris")
plt.figure()
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df)
plt.title("Iris Sepal vs Petal")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
