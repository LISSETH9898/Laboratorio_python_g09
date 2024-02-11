
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

def multiplo(num1,num2):
    if num2 % num1 == 0:
        print("el segundo numero {} es multiplo de {} ".format(num2,num1))
    elif num1 % num2 == 0:
        print("el primer numero {} es multiplo de {} ".format(num1, num2))
    return

mul = multiplo(num1,num2)


