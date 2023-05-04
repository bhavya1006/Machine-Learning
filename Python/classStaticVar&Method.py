# creating a class name Student
class Student:
    
    # Making Documentation of Student class
    "This is the Student Class DOcUMENtaion where name, id and cgpa can be stored and be displayed respectively."
    
    # class variable
    _institute = 'MITS'
    SNo = 0

    # creating constructor
    def __init__(self,name,id,cgpa):
        Student.SNo += 1
        self.name=name
        self._id=id
        self.__cgpa=cgpa
    
    # making return for class Student (as replace for location)
    def __str__(x):
        return "\n\nSerial No."+str(s1.SNo)+"\nName: "+x.name+"\nID: "+str(x._id)+"\nCGPA: "+str(x.__cgpa)+"\nInstitute: "+Student._institute
      
    # checking destructor
    def __del__(x):
        print("**Destructor Called**")
        
    # creating a function to display
    def display(y):
        print('Name',y.name,'ID',y._id,'CGPA',y.__cgpa)
        return

    # creating function to take input
    def insert(x):
        Student.SNo += 1
        x.name=input("enter name:")
        x._id=input("enter id:")
        x.__cgpa=input("enter cgpa:")
        return
    
    # using static method
    @staticmethod
    def chkCGPA(y):
        if y.__cgpa>9:
            return True
        return False

# creating object s1 in class Student
s1 = Student("Nishchay",45,9.2)
print("S1 Object:",s1)

# creating object s2 in class Student
s2 = Student("Mythpat",39,8)
print("S2 Object:",s2)

# Static method used
print(Student.chkCGPA(s1))
print(Student.chkCGPA(s2))