# Boxplot - Marks by Class
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "07_boxplot.png")
rng = np.random.default_rng(2)
a = rng.normal(70, 8, 50)
b = rng.normal(80, 8, 50)
plt.figure()
plt.boxplot([a, b], tick_labels=["Class A", "Class B"])
plt.title("Marks by Class")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
