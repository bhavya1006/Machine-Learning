""" 
    Write A Program to represent student using OOPs where each student is prepared by name, id, cgpa and semester.
    The student class to be implemented should contain all the necessary function appropriate for a student. The 
    class should contain 3 dictionary variables as static memebers which should contain the topper list of each 
    semester (assume 1, 2& 3). The key in each dictionary should represent all the details of a particular 
    students.
"""


# creating a class name Student
class Student:

    # creating static variable dict & list for storing rank wise name of students
    __dict1 = dict()
    __dict2 = dict()
    __dict3 = dict()

    # creating list to store input value and sort later
    __list1 = []
    __list2 = []
    __list3 = []

    # creating a constructor
    def __init__(self,name,id,cgpa,semester):
        self.__detail = [cgpa,name,id,semester]

        # checking and storing detail in respective semester list
        if semester == 1:
            Student.__list1.append(self.__detail)
        elif semester == 2:
            Student.__list2.append(self.__detail)
        else:
            Student.__list3.append(self.__detail)
    
    # defining a static function
    @staticmethod
    def displayMeritList():

        # sorting list and storing as rankwise in dictionary
        Student.__list1.sort(reverse=True)
        for i, x in enumerate(Student.__list1):
            Student.__dict1[i+1] = x

        # sorting list and storing as rankwise in dictionary
        Student.__list2.sort(reverse=True)
        for i, x in enumerate(Student.__list2):
            Student.__dict2[i+1] = x

        # sorting list and storing as rankwise in dictionary
        Student.__list3.sort(reverse=True)
        for i, x in enumerate(Student.__list3):
            Student.__dict3[i+1] = x
        
        # displaying result
        print("Semester 1: ",Student.__dist1)
        print("Semester 2: ",Student.__dict2)
        print("Semester 3: ",Student.__dict3)

# menu-code
while True:

    # using try-except to take a valid choice
    try:
        c = int(input("1-Registor.\n2-Exit.\nEnter Your Choice: "))
    except:
        print("Please Enter a Valid Choice!!")
        continue                                               # this will continue the while from start

    if c==1:
        # creating object "s" 
        s = Student(input("Name: "),input("ID: "),float(input("CGPA: ")),int(input("Semester: ")))
        continue                                               # this will continue the while from start
    elif c==2:
        # accessing static function
        Student.displayMeritList()
        break                                               # this will break the while to exit
    else:
        print("Please Enter a Valid Choice!!")
        continue                                               # this will continue the while from start
