file = open("employee_info.txt",'r')
emp_Detail = list()

for lines in file.readlines():
    emp_Detail.append(lines.split(','))

def tax_to_be_deposit(emp_det):
    provident_fund = int(emp_det[3])
    salary = int(emp_det[2])
    tax_deposited = int(emp_det[4])
    tax = 0
    if provident_fund>=150000:
        salary-=provident_fund
        if salary<=500000:
            tax = salary*0.05
        elif salary>=500000 and salary<=750000:
            tax = salary*0.10
        elif salary>=750000 and salary<=1000000:
            tax = salary*0.15
        elif salary>=1000000:
            tax = salary*0.20
        
        if tax > tax_deposited:
            return tax - tax_deposited
        else:
            return tax_deposited - tax
    else:
        return tax

emp_DetailsDic = dict()
for i in emp_Detail:
    emp_DetailsDic[i[1]] = tax_to_be_deposit(i)
print(emp_DetailsDic)

file = open("employee_tax.txt",'w')
for i in emp_Detail:
    file.write(i[0]+','+i[1]+','+str(tax_to_be_deposit(i))+','+'\n')
file.close()
file = open("employee_tax.txt",'r')
all = file.read()
print(all)
file.close()
