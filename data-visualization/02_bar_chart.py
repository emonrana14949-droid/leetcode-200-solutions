# Bar Chart - Sales by City
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "02_bar_chart.png")
cities = ["Dhaka", "Sylhet", "Khulna", "Rajshahi"]
sales = [120, 80, 60, 40]
plt.figure()
plt.bar(cities, sales)
plt.title("Sales by City")
plt.ylabel("Sales")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
