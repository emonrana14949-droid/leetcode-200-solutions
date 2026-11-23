# Seaborn Barplot - Tips by Sex
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "31_barplot_seaborn.png")
import seaborn as sns
df = sns.load_dataset("tips")
plt.figure()
sns.barplot(x="sex", y="total_bill", data=df)
plt.title("Average Bill by Sex")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
