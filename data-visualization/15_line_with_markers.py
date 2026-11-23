# Line Chart with Markers - Temperature
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "15_line_with_markers.png")
days = list(range(1, 8))
temp = [30, 32, 31, 33, 35, 34, 36]
plt.figure()
plt.plot(days, temp, marker="s", linestyle="--")
plt.title("Dhaka Temperature (7 days)")
plt.xlabel("Day")
plt.ylabel("Celsius")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
