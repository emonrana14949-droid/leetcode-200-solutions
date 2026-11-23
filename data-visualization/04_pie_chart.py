# Pie Chart - Market Share
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "04_pie_chart.png")
labels = ["A", "B", "C", "D"]
sizes = [40, 30, 20, 10]
plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.0f%%")
plt.title("Market Share")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
