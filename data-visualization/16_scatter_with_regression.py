# Scatter with Regression Line
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "16_scatter_with_regression.png")
import seaborn as sns
import pandas as pd
df = pd.DataFrame({"hours": [1, 2, 3, 4, 5], "marks": [50, 60, 65, 75, 85]})
plt.figure()
sns.regplot(x="hours", y="marks", data=df)
plt.title("Hours vs Marks")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
