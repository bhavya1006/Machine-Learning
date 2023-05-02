# creating a class name Student
class Student:
    
    
    # creating constructor
    def __init__(self):
        self.name=''
        self._id=0
        self.__cgpa=0.0
    
    # making return for class Student (as replace for location)
    def __str__(x):
        return "Name: "+x.name+" ID: "+str(x._id)+" CGPA: "+str(x.__cgpa)
      
    # checking destructor
    def __del__(x):
        print("Destructor Called")
        
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
s1 = Student()

# checking constructor 
print("S1 Object:",s1)
# s1.display() --> as s1 will be displaying 

# inserting value and displaying
s1.insert()
print(s1)
