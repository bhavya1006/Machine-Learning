class Fraction:

    def __init__(self,p,q):
        self.__num = p
        self.__den = q

    def display(self):
        print("Number is",self.__num,"/",self.__den)
    
    def __add__(self,other):
        return Fraction(self.__num*other.__den + self.__den*other.__num , self.__den*other.__den)
    
    def __sub__(self,other):
        return Fraction(self.__num*other.__den - self.__den*other.__num , self.__den*other.__den)
    
    def __mul__(self,other):
        return Fraction(self.__num*other.__num,self.__den*other.__den)
    
    def __ge__(self,other):
        return True if self.__num*other.__den >= self.__den*other.__num else False
    
    def __le__(self,other):
        return True if self.__num*other.__den <= self.__den*other.__num else False
    

f1 = Fraction(3,4)
f2 = Fraction(4,5)

print("Addition Overloading: ")
f = f1 + f2 
f.display()
print("Subtraction Overloading: ")
f = f1 - f2
f.display()
print("Multiplication Overloading: ")
f = f1 * f2
f.display()

print("Greater than equal to Overloading: ")
print(f1>=f2)
print("Smaller than equal to Overloading: ")
print(f1<=f2)