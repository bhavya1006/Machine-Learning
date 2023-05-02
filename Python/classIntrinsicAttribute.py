# creating a class name Student
class Student:
    
    # Making Documentation of Student class
    "This is the Student Class DOcUMENtaion where name, id and cgpa can be stored and be displayed respectively."
    
    # creating constructor
    def __init__(self,name,id,cgpa):
        self.name=name
        self._id=id
        self.__cgpa=cgpa
    
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
s1 = Student("Nishchay",45,9.2)

# checking constructor 
print("S1 Object:",s1)
print()


print("Documentation of the class Student: ",Student.__doc__)
print("\nName of the class Student: ",Student.__name__)
print("\nModule of the class Student: ",Student.__module__)
print("\nBases of the class Student: ",Student.__bases__)
print("\nALL Info of the class Student in dictionary: ",Student.__dict__)


print("\nOrigin of the object from which class: ",s1.__class__)
