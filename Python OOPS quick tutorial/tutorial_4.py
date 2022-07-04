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

    #class method
    @classmethod
    def change_increment(cls, amount):
        cls.increment = amount

    @classmethod
    def from_str(cls,emp_string):
        fname , lname , salary = emp_string.split("-")
        return cls(fname,lname,salary)




harry = Employee('harry', 'jackson', 44000)
lovish = Employee.from_str("lovish-jackson-76000")
rohan = Employee('rohan', 'xyz', 74000)

print(lovish.fname)