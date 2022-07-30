ano = 1
ninero = 1000
interes = 0

while año <= 7:
    interes = ninero * 0.05
    ninero = ninero + interes
    ano += 1
    print(ninero)