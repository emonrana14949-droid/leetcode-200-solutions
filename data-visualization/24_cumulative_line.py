# Cumulative Line - Total Rain
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "24_cumulative_line.png")
rain = [5, 10, 0, 20, 15]
plt.figure()
plt.plot(np.cumsum(rain), marker="o")
plt.title("Cumulative Rainfall")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
