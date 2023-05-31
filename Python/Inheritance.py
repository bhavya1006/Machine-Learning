class Person:

    def __init__(s,name,age,gender,address):
        s.name = name
        s.age = age
        s.gender = gender
        s.address = address

    def display(s):
        print(f'Name: {s.name} Age: {s.age} Gender: {s.gender} Address: {s.address}')

class Employee(Person):

    __empId = 'C000{}'

    def __init__(s,empId,salary,designation,n,a,g,add):
        s.empId = Employee.__empId.format(empId)
        s.salary = salary
        s.desg = designation
        Person.__init__(s,n,a,g,add)

    def display(s):
        print(f"Employee Id: {s.empId} Salary: {s.salary} Designation: {s.desg}")
        super().display()

class admin(Employee):

    def __init__(s,access,e,sal,d,n,a,g,add):
        s.access = access
        Employee.__init__(s,e,sal,d,n,a,g,add)
    
    def display(s):
        print(f"Admin Permit: {s.access}")
        super().display()


master = admin("Yes",25,34900,"Sen. Developer","Arya Kohli",28,'F',"Gwalior")
master.display()
