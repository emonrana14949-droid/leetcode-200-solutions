# 200 Problems — Python, NumPy, Pandas, SQL, Data Visualization & ML

Hi, I am **Md Emon Rana**, a final-year CSE student at Southeast University, Dhaka. 
This repo is my practice collection — 200 small problems I solved myself, one file per problem, 
so I can revise Python, NumPy, Pandas, SQL, charts and ML in one place.

## How to run

```bash
pip install -r requirements.txt
python run_all.py          # runs all 200 problems, Python + SQL
python python/01_two_sum.py   # run one problem
python sql/create_db.py    # rebuild the sample SQLite database
```

SQL problems run on the small sample database in `sql/sample.db` 
(employees, departments, customers, orders) — created by `sql/create_db.py`.

## Problems by area

| Area | Problems | What is inside |
| --- | --- | --- |
| Python | 34 | core Python, strings, lists, dicts, functions, classes, a few classic algorithms |
| NumPy | 33 | arrays, vectorization, broadcasting, linear algebra |
| Pandas | 33 | filtering, groupby, merge, pivot, time series |
| SQL | 34 | SELECT, JOIN, GROUP BY, HAVING, subqueries, window functions |
| Data Visualization | 33 | Matplotlib + Seaborn charts, each one saves a PNG in `outputs/` |
| Machine Learning | 33 | scikit-learn: regression, classification, clustering, metrics, pipelines |
| **Total** | **200** | |

## Note

These are practice solutions, written in my own simple style. 
Datasets are small and built-in (scikit-learn datasets, or tiny sample tables I made) 
so every file runs without the internet.
