# Seaborn Lineplot - Flights Passengers
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "30_lineplot_seaborn.png")
import seaborn as sns
df = sns.load_dataset("flights")
plt.figure()
sns.lineplot(x="year", y="passengers", data=df)
plt.title("Air Passengers by Year")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
