# Time Series - Daily Visitors
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "23_time_series.png")
import pandas as pd
idx = pd.date_range("2024-01-01", periods=30, freq="D")
vals = np.arange(30) + 100
plt.figure()
plt.plot(idx, vals)
plt.title("Daily Visitors")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
