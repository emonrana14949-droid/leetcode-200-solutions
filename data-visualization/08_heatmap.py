# Heatmap - Correlation Matrix
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "08_heatmap.png")
import seaborn as sns
data = np.array([[1, 0.8, 0.2], [0.8, 1, 0.5], [0.2, 0.5, 1]])
plt.figure()
sns.heatmap(data, annot=True, vmin=0, vmax=1)
plt.title("Correlation Heatmap")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
