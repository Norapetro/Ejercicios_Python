def numPar_Multiplo(numero):
    return numero % 2 == 0 and numero % 6 == 0

def main():
    numero = int(input("Ingrese un número: "))
    if numPar_Multiplo(numero):
        print(f"{numero} es par y múltiplo de 6.")
    else:
        print(f"{numero} no cumple con las condiciones.")

if __name__ == "__main__":
    main()
