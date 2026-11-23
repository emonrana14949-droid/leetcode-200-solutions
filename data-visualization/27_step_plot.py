# Step Plot - Price Steps
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "27_step_plot.png")
x = [1, 2, 3, 4, 5]
y = [100, 100, 120, 120, 140]
plt.figure()
plt.step(x, y, where="mid")
plt.title("Rice Price Steps")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
