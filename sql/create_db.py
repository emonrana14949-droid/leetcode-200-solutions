"""Create the sample SQLite database (sample.db) for the SQL problems."""
import os, sqlite3
DB = os.path.join(os.path.dirname(__file__), "sample.db")
if os.path.exists(DB):
    os.remove(DB)
con = sqlite3.connect(DB)
cur = con.cursor()
cur.executescript("""
CREATE TABLE departments (name TEXT, location TEXT);
CREATE TABLE employees (id INTEGER, name TEXT, department TEXT, job_title TEXT, salary INTEGER, manager_id INTEGER);
CREATE TABLE customers (id INTEGER, name TEXT);
CREATE TABLE orders (id INTEGER, customer_id INTEGER, product TEXT, amount INTEGER, order_date TEXT);
INSERT INTO departments VALUES ('Sales', 'Dhaka'), ('IT', 'Dhaka'), ('HR', 'Chittagong'), ('Finance', 'Sylhet');
INSERT INTO employees VALUES
 (1, 'Asha', 'Sales', 'Sales Executive', 55000, 3),
 (2, 'Babu', 'IT', 'Developer', 70000, 3),
 (3, 'Chadni', 'HR', 'Manager', 90000, NULL),
 (4, 'David', 'Sales', 'Sales Executive', 45000, 1),
 (5, 'Emon', 'IT', 'Developer', 65000, 3),
 (6, 'Farah', 'HR', 'Recruiter', 40000, 3),
 (7, 'Arif', 'Sales', 'Manager', 80000, NULL),
 (8, 'Nusrat', 'IT', 'Developer', 60000, 2);
INSERT INTO customers VALUES (1, 'Rahim'), (2, 'Karim'), (3, 'Salma'), (4, 'Tanvir');
INSERT INTO orders VALUES
 (1, 1, 'Rice', 120, '2024-01-05'),
 (2, 1, 'Oil', 80, '2024-01-12'),
 (3, 2, 'Rice', 200, '2024-01-20'),
 (4, 3, 'Tea', 50, '2024-02-03'),
 (5, 2, 'Sugar', 150, '2024-02-10'),
 (6, 1, 'Rice', 90, '2024-03-01');
""")
con.commit()
con.close()
print("sample.db created")
