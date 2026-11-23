# Sort by Key - sort students by marks, highest first.
def sort_students(students):
    return sorted(students, key=lambda s: s["marks"], reverse=True)

if __name__ == "__main__":
    s = [{"name": "A", "marks": 70}, {"name": "B", "marks": 90}, {"name": "C", "marks": 80}]
    assert [x["name"] for x in sort_students(s)] == ["B", "C", "A"]
    print("ok")
