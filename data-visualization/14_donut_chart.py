# Donut Chart - Expenses
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "14_donut_chart.png")
sizes = [40, 30, 20, 10]
plt.figure()
plt.pie(sizes, labels=["Food", "Rent", "Travel", "Other"], wedgeprops=dict(width=0.4))
plt.title("Monthly Expenses")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
