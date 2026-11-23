# Scatter Plot - Hours vs Marks
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "05_scatter_plot.png")
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([50, 55, 65, 70, 80, 85])
plt.figure()
plt.scatter(x, y)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
