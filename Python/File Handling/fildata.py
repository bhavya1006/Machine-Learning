try:
    file = open("student_info.txt",'r')
    content = []
    while (True):
        x = file.readlines()
        if x!='':
            content.append(x.split(','))
        else:
            break
except Exception as a:
    print("Exception, Error message:",a)

else:
    content.remove(['\n'])
    semList = []

    for x in content:
        if (int(x[2]) not in semList):
            semList.append(int(x[2]))
    for x in semList:
        l2 = []
        for y in content:
            if (y[2]==x):
                l2.append(str(float(y[3]))+','+y[0]+','+y[1]+','+y[2])
        
        print("Semester: ",x)
        l2.sort(reverse=True)
        for z in l2:
            temp = z.split(',')
            print("Name:",temp[1],"Enrolment Id:",temp[2],"CGPA:",temp[0])