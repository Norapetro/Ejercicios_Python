while True:
    numero = int(input("Escriba un número positivo de 3 cifras: "))

    if numero >= 100 and numero <=999:
        print("Ingresó el numero: ", numero, "Gracias")
        break  
    else:
        print("Inténtelo nuevamente.")