print("La forma canónica de la ecuación cuadrática es: \n ax^2 + bx + c = 0")
print("Introduzca los coeficientes: ")

a = input("a = ")
b = input("b = ")
c = input("c = ")

#Cast a int() desde str(), formato de input por default
a = int(a)
b = int(b)
c = int(c)

x1 = (-b + ((b**2)-4*a*c)**(1/2))/(2*a)
x2 = (-b - ((b**2)-4*a*c)**(1/2))/(2*a)

print("x1 = ","{0:.3f}".format(x1))
print("x2 = ","{0:.3f}".format(x2))