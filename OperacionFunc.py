def suma(arg1,arg2):
    R = int(arg1) + int(arg2)
    return (R)

def resta(arg1,arg2):
    R = int(arg1) - int(arg2)
    return (R)

def multiplicacion(arg1,arg2):
    R = int(arg1) * int(arg2)
    return (R)

def division(arg1,arg2):
    arg1 = int(arg1)
    arg2 = int(arg2)
    if(arg2 != 0):
        R = arg1 / arg2
    else:
        print("La operacion a realizar no esta definida")
        R = "nan"
    return (R)



Bool = "Si"
while(Bool == "Si"):

    a = input("Introduzca primer sumando: ")
    b = input("Introduzca segundo sumando: ")
    Op = input("Que operacion desea realizar? ")

    if(Op == "Suma"):
        print("El resultado es {}".format(suma(a,b)))

    elif(Op == "Resta"):
        print("El resultado es {}".format(resta(a,b)))

    elif(Op == "Multiplicacion"):
        print("El resultado es {}".format(multiplicacion(a,b)))

    elif(Op == "Division"):
        print("El resultado es {}".format(division(a,b)))

    else:
        print("Debe introducir una operacion valida")

    Bool = input("¿Desea realizar otra operacion? ")


