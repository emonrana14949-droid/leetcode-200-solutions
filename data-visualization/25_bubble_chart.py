# Bubble Chart - Population vs GDP
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "25_bubble_chart.png")
x = [170, 1400, 240]
y = [400, 3500, 340]
sizes = [200, 800, 300]
plt.figure()
plt.scatter(x, y, s=sizes, alpha=0.5)
plt.xlabel("Population (M)")
plt.ylabel("GDP (B USD)")
plt.title("Population vs GDP")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
