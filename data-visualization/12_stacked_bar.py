# Stacked Bar - Sales by Quarter
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "12_stacked_bar.png")
q = ["Q1", "Q2", "Q3", "Q4"]
a = [20, 25, 22, 30]
b = [15, 18, 20, 25]
plt.figure()
plt.bar(q, a, label="Online")
plt.bar(q, b, bottom=a, label="Shop")
plt.legend()
plt.title("Sales by Quarter")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
