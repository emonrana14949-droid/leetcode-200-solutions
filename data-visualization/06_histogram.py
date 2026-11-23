# Histogram - Marks Distribution
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "06_histogram.png")
rng = np.random.default_rng(1)
data = rng.normal(70, 10, 200)
plt.figure()
plt.hist(data, bins=15)
plt.title("Marks Distribution")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
