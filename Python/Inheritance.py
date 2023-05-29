class Person:
    def __init__(s,n,age):
        s.name=n
        s.age=age
    def display(s):
        print(s.name,s.age,end=' ')
class Emp(Person):
    def __init__(s,salary,n,a):
        Person.__init__(s,n,a)
        s.salary = salary
    def display(s):
        super().display()
        print(s.salary)
class admin(Emp):
    def __init__(s,pre,n,a,sal):
        s.pre=pre
        Emp.__init__(s,sal,n,a)
    def display(s):
        print(s.pre)
        super().display()
        
a = admin("5g%##",34000,"guru",34)
ab = admin("6/^&%",45002,"pita",51)

a.display()
ab.display()