"""Run all 200 problems and report pass/fail.

Python problems: run each .py file as a script (it has asserts in __main__).
SQL problems: run each .sql file on sql/sample.db (rebuilt first).
Usage: python run_all.py
Use the project venv so sklearn/pandas/seaborn are available.
"""
import os, subprocess, sys, sqlite3

ROOT = os.path.dirname(os.path.abspath(__file__))
PY_FOLDERS = ["python", "numpy", "pandas", "data-visualization", "ml"]

def run_py(path):
    r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=120)
    return r.returncode == 0, (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout + r.stderr).strip() else ""

def main():
    # rebuild the sample DB first
    subprocess.run([sys.executable, os.path.join(ROOT, "sql", "create_db.py")], check=True, capture_output=True)
    passed, failed = [], []
    for folder in PY_FOLDERS:
        d = os.path.join(ROOT, folder)
        for name in sorted(os.listdir(d)):
            if name.endswith(".py"):
                p = os.path.join(d, name)
                ok, msg = run_py(p)
                (passed if ok else failed).append(f"{folder}/{name} {msg}")
    con = sqlite3.connect(os.path.join(ROOT, "sql", "sample.db"))
    cur = con.cursor()
    sql_dir = os.path.join(ROOT, "sql")
    for name in sorted(os.listdir(sql_dir)):
        if name.endswith(".sql"):
            sql = open(os.path.join(sql_dir, name)).read()
            try:
                cur.execute(sql)
                rows = cur.fetchall()
                if rows:
                    passed.append(f"sql/{name} ({len(rows)} rows)")
                else:
                    failed.append(f"sql/{name} (no rows)")
            except Exception as e:
                failed.append(f"sql/{name} ERROR {e}")
    con.close()
    print(f"PASSED: {len(passed)}/200")
    print(f"FAILED: {len(failed)}/200")
    for x in failed:
        print("FAIL:", x)
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
