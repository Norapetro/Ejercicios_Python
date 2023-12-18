while True:
    numero = input("Ingrese un número en la calculadora (o 's' para salir): ")
    
   
    if numero.lower() == 's':
        print("¡Adios!")
        break

         
    num = int(numero)
    
    print(f"Tabla del {num}:")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
