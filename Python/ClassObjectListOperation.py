class Student:
    __count = 0
    
    def __init__(s):
        s.__name=''
        s.__id = 0
        s.__cgpa = 0.0
        Student.__count += 1
    
    @staticmethod
    def displayNoStudent():
        print("Number of Students regitered till date: ",Student.__count)
    
    def setValues(s):
        s.__name = input("Enter Your Name: ")
        s.__id = int(input("Enter Your ID: "))
        s.__cgpa = float(input("Enter Your CGPA: "))
    
    def disValues(s):
        print(f"{s.__id}. {s.__name} scored {s.__cgpa}")

Student.displayNoStudent()
objList = []

while True:
    ch = int(input("Enter 1 to register.\nEnter 2 for display.\nEnter 3 To exit.\n"))

    if ch == 1:
        stu = Student()
        stu.setValues()
        objList.append(stu)

    elif ch == 2:
        ch2 = int(input("Enter 4 to display particular student.\nEnter 5 to display all.\n"))

        if ch2 == 4:
            objList[int(input("Enter position: "))-1].disValues()
        else:
            for i in objList:
                i.disValues()
    else:
        break
Student.displayNoStudent()
