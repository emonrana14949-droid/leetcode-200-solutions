# Subplots 2x2 - Four Charts in One
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "19_subplots_2x2.png")
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
axes[0, 0].plot([1, 2, 3], [1, 2, 3])
axes[0, 1].bar(["a", "b"], [1, 2])
axes[1, 0].scatter([1, 2], [3, 4])
axes[1, 1].pie([30, 70])
fig.suptitle("Four Charts")
plt.tight_layout()
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
