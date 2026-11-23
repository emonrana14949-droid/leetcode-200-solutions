# Bar Chart with Error Bars
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "17_bar_with_error_bars.png")
means = [70, 80, 75]
errs = [5, 4, 6]
plt.figure()
plt.bar(["A", "B", "C"], means, yerr=errs, capsize=5)
plt.title("Mean Marks with Error")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
