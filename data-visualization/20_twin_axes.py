# Twin Axes - Sales and Profit
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "20_twin_axes.png")
x = [1, 2, 3, 4]
sales = [100, 150, 130, 180]
profit = [20, 30, 25, 40]
fig, ax1 = plt.subplots()
ax1.plot(x, sales, "b-")
ax1.set_ylabel("Sales", color="b")
ax2 = ax1.twinx()
ax2.plot(x, profit, "r-")
ax2.set_ylabel("Profit", color="r")
plt.title("Sales and Profit")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
