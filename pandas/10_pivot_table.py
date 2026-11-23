# Pivot Table - total sales by city and product.
import pandas as pd
def pivot():
    df = pd.DataFrame({"city": ["Dhaka", "Dhaka", "Sylhet"], "item": ["a", "b", "a"], "sales": [10, 20, 30]})
    return df.pivot_table(index="city", columns="item", values="sales", aggfunc="sum", fill_value=0)

if __name__ == "__main__":
    p = pivot()
    assert p.loc["Dhaka", "a"] == 10 and p.loc["Sylhet", "a"] == 30
    print("ok")
