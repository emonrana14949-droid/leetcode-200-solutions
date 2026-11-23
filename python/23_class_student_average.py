# Class - a Student class that stores marks and returns the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks) / len(self.marks)

if __name__ == "__main__":
    s = Student("Emon", [80, 90, 70])
    assert s.average() == 80.0
    print("ok")
