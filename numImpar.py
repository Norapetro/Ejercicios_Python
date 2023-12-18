class Num_Impar:
    def __init__(self, numero):
        self.numero = numero

    def Num_Impar(self):
        return self.numero % 2 != 0 and self.numero % 5 == 0

def main():

    numero_ingresado = int(input("Ingrese un número: "))
    verificador = Num_Impar(numero_ingresado)

    if verificador.Num_Impar():
        print(f"{numero_ingresado} es impar y múltiplo de 5.")
    else:
        print(f"{numero_ingresado} no cumple con las condiciones.")

if __name__ == "__main__":
    main()