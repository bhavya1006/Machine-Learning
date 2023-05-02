# creating a class name student

class student:
    # creating constructor
    def __init__(self):
        self.name=''
        self._id=0
        self.__cgpa=0.0
    # creating a function to display
    def display(y):
        print('Name',y.name,'ID',y._id,'CGPA',y.__cgpa)
        return
    # creating function to take input
    def insert(x):
        x.name=input("enter name:")
        x._id=input("enter id:")
        x.__cgpa=input("enter cgpa:")
        return

# creating object s1 in class student
s1 = student()
# checking constructor 
print("S1 Object:",s1)
s1.display()

# inserting value and displaying
s1.insert()
s1.display()
