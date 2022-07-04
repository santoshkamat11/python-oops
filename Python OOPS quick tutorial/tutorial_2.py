class Employee:

    increment = 1.5
    no_of_employees = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.no_of_employees +=1

    def increase(self):
        #self.increment will search for the properties of instance followed by class property
        self.salary = int(self.salary * self.increment)



print("initial no of employees is ",Employee.no_of_employees)
harry = Employee('harry', 'jackson', 10)
rohan = Employee('rohan', 'xyz', 10)
print("final no of employees is ",Employee.no_of_employees)

print("name is ",harry.fname)
print("rohans salary before increment is ",rohan.salary)
rohan.increase()
print("after increment rohans salary is ",rohan.salary)

print("printing all properties of rohan instance")
print(rohan.__dict__)
rohan.batting = "batting"
rohan.salary = 18
print("printing all added/changed properties of rohan instance")
print(rohan.__dict__)

print("getting all properties of Employee class")
print(Employee.__dict__)