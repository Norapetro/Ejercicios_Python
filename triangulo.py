i = 0
while i <= 5:
    print(i * " * ")
    i = i + 1
    
    
def triangulo(filas):
    for ite in range(1, filas * 2, 2):
        for j in range(ite, 0, -2):
            print(j, end=" ")
        print()

filas = 5
triangulo(filas)
