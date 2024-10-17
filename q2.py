class Employee:
    def __init__(self, name, idNum, dept, jobTitle):
        assert type(name) == type(""), "name should be a python string"
        assert type(idNum) == type(1), "idNum should be a python integer"
        assert type(dept) == type(""), "dept should be a python string"
        assert type(jobTitle) ==  type(""), "jobTitle should be a python string"

        self.name = name
        self.idNum = idNum
        self.dept = dept
        self.jobTitle = jobTitle
    
    def __str__(self):
        return "<object:Employee\n\
 Name: "+self.name+"\n\
 ID Number: "+str(self.idNum)+"\n\
 Department: "+self.dept+"\n\
 Job Title: "+self.jobTitle+"\n\
>"

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print(emp1)
print(emp2)
print(emp3)