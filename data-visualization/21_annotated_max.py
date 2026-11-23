# Annotated Chart - Mark the Highest Point
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "21_annotated_max.png")
x = [1, 2, 3, 4, 5]
y = [10, 25, 15, 30, 20]
plt.figure()
plt.plot(x, y, marker="o")
plt.annotate("max", xy=(4, 30), xytext=(3, 32), arrowprops=dict(arrowstyle="->"))
plt.title("Sales with Max Marked")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
