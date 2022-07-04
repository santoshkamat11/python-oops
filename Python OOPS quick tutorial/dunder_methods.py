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

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True

    #dunder method
    def __add__(self, other):
        return self.salary + other.salary

    #dunder method
    def __repr__(self):
        return 'Employee ({} , {} , {})'.format(self.fname,self.lname,self.salary)

    #dunder method
    def __str__(self):
        return 'the name of the employee is {}'.format(self.fname)


a=6
print(a.__add__(7))
print(a.__mul__(9))

harry = Employee('harry','jackson',230)
rohan = Employee('rohan','agrawal',900)

print(harry.__add__(rohan))
print(harry + rohan)

#following runs dunder method repr
print(rohan)

print(repr(rohan))
print(str(rohan))

# str has more preference than repr