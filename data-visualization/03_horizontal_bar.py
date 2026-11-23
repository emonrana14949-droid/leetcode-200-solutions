# Horizontal Bar Chart - Top Products
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "03_horizontal_bar.png")
items = ["Rice", "Oil", "Sugar", "Tea"]
vals = [50, 40, 30, 20]
plt.figure()
plt.barh(items, vals)
plt.title("Top Products")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
