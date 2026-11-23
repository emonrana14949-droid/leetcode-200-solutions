# Area Chart - Cumulative Sales
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "11_area_chart.png")
x = [1, 2, 3, 4, 5]
y = [10, 25, 38, 58, 83]
plt.figure()
plt.fill_between(x, y)
plt.title("Cumulative Sales")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
