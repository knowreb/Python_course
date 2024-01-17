class Emplyee():
    """Information about name, last name, and salary"""
    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.salary += amount