# Histogram with KDE
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "18_histogram_kde.png")
import seaborn as sns
rng = np.random.default_rng(4)
data = rng.normal(70, 10, 200)
plt.figure()
sns.histplot(data, kde=True, bins=15)
plt.title("Marks with KDE")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
