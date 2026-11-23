# Stem Plot - Monthly Rainfall
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "26_stem_plot.png")
x = list(range(1, 13))
y = [10, 20, 40, 80, 150, 300, 400, 350, 200, 80, 20, 5]
plt.figure()
plt.stem(x, y)
plt.title("Monthly Rainfall (mm)")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
