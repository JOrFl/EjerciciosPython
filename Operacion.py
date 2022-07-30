Op = input("Que operacion desea realizar? ")

if(Op == "Suma"):
    a = input("Introduzca primer sumando: ")
    b = input("Introduzca segundo sumando: ")
    R = int(a) + int(b)
elif(Op == "Resta"):
    a = input("Introduzca minuendo: ")
    b = input("Introduzca sustraendo: ")
    R = int(a) - int(b)
elif(Op == "Multiplicacion"):
    a = input("Introduzca el primer factor: ")
    b = input("Introduzca el segundo factor: ")
    R = int(a) * int(b)
elif(Op == "Division"):
    a = int(input("Introduzca dividendo: "))
    b = int(input("Introduzca divisor: "))
    if(b != 0):
        R = a / b
    else:
        print("La operacion a realizar no esta definida")
        R = "nan"


print("El resultado es: ", R)