# Sorted Bar Chart - Countries by Population
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "22_sorted_bar.png")
data = {"Bangladesh": 170, "India": 1400, "Pakistan": 240, "Nepal": 30}
items = sorted(data.items(), key=lambda kv: kv[1])
plt.figure()
plt.bar([k for k, _ in items], [v for _, v in items])
plt.title("Population (millions)")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
