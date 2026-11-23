# Grouped Bar - Boys vs Girls Marks
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
OUT = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUT, exist_ok=True)
PATH = os.path.join(OUT, "13_grouped_bar.png")
import numpy as np
x = np.arange(3)
plt.figure()
plt.bar(x - 0.2, [70, 80, 75], width=0.4, label="Boys")
plt.bar(x + 0.2, [75, 85, 80], width=0.4, label="Girls")
plt.xticks(x, ["Math", "English", "Science"])
plt.legend()
plt.title("Marks by Subject")
plt.savefig(PATH)
plt.close()

if __name__ == "__main__":
    assert os.path.exists(PATH) and os.path.getsize(PATH) > 0
    print("ok")
