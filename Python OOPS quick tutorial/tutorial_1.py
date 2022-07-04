class Employee:

    increment = 1.5

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def increase(self):
        self.salary = int(self.salary * Employee.increment)




harry = Employee('harry', 'jackson', 10)
rohan = Employee('rohan', 'xyz', 10)

print("name is ",harry.fname)
print("rohans salary before increment is ",rohan.salary)
rohan.increase()
print("after increment rohans salary is ",rohan.salary)
