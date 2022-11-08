#Clase
class Fraction():
    ##Atributos##
    numerator = 0
    denominator = 0
    ##Fin Atributos##

    ##Constructor##
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    ##Fin Constructor##
    
    ##Metodos##
    def multiplication(self,other):
        other.denominator = self.denominator * other.denominator       
        self.denominator = self.numerator * other.numerator
        mcma = self.mcm(other,1,0,0)
        numerator = self.denominator/mcma
        denominator = other.denominator/mcma
        print("\nEl resultado de la multiplicacion:",numerator,"/",denominator)
    
    def division(self,other):
        other.denominator = self.numerator * other.denominator
        self.denominator = self.denominator * other.numerator
        mcma = self.mcm(other,1,0,0)
        numerator = other.denominator/mcma
        denominator = self.denominator/mcma
        print("\nEl resultado de la division:",numerator,"/",denominator)
    
    def mcm(self,other,i,b,c):
        if((self.denominator!=0)and(i != 0)):
            temp = 0
            i = other.denominator
            a = self.denominator
            while(i != 0):
                temp = i
                i = a % i
                a = temp
            return(a)
        elif(i==0):
            temp = 0
            i = b
            a = c
            while(i != 0):
                temp = i
                i = a % i
                a = temp
            return(a)            
    
    def addition(self,other):
        if(self.denominator != other.denominator):
            denominantor = (self.denominator * other.denominator)
            numerator = (self.numerator*other.denominator)+(other.numerator*self.denominator)
            mcma = self.mcm(other,0,denominantor,numerator)
            numerator = numerator/mcma
            denominator = denominantor/mcma
            print("\nEl resultado de la suma:",numerator,"/",denominator)
        else:
            numerator = self.numerator + other.numerator
            print("\nEl resultado de la suma:",numerator,"/",self.denominator)

    def subtraction(self,other):
        if(self.denominator != other.denominator):
            denominantor = (self.denominator * other.denominator)
            numerator = (self.numerator*other.denominator)-(other.numerator*self.denominator)
            mcma = self.mcm(other,0,denominantor,numerator)
            numerator = numerator/mcma
            denominator = denominantor/mcma
            print("\nEl resultado de la resta:",numerator,"/",denominator)
        else:
            numerator = self.numerator - other.numerator
            print("\nEl resultado de la resta:",numerator,"/",self.denominator)


#Iniciar variables
numerator_1 = 0
numerator_2 = 0
denominator_1 = 0
denominator_2 = 0
f_1 = 0
f_2 = 0
opcion = 0
#Entrada de datos
numerator_1 = int(input("Numerador fraccion A: "))
while(denominator_1 == 0):
    denominator_1 = int(input("Denomiador fraccion A: "))
    if(denominator_1!=0):
        break
    print("Ingrese un denominador distinto de 0")
numerator_2 = int(input("Numerador fraccion B: "))
while(denominator_2 == 0):
    denominator_2 = int(input("Denomiador fraccion B: "))
    if(denominator_2!=0):
        break
    print("Ingrese un denominador distinto de 0")
#asignar variables
f_1 = Fraction(numerator_1, denominator_1)
print("Fraccion A =",f_1.numerator,"/",f_1.denominator)
f_2 = Fraction(numerator_2, denominator_2)
print("Fraccion B =",f_2.numerator,"/",f_2.denominator)
#Menu
print("\n---------OPERACIONES MATEMATICAS CON FRACCIONES---------\n")
print("SUMA(+)")
print("RESTA(-)")
print("MULTIPLICACION(*)")
print("DIVISION(/)\n")
print("---------------------------------------------------------\n")
opcion = input("Ingrese la operacion a realizar (+ - * /):")

match(opcion):
    case '+':
        f_1.addition(f_2)
    case '-':
        f_1.subtraction(f_2)
    case '*':
        f_1.multiplication(f_2)
    case '/':
        f_1.division(f_2)
