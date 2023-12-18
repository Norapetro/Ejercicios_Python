mesActual = int(input("Ingrese el mes actual: "))
anioActua = int(input("Ingrese el año actual: "))
mesNacimiento = int(input("Ingrese el mes de nacimiento: "))
anioNacimiento = int(input("Ingrese el año de nacimiento: "))
edad = anioActua - anioNacimiento
if mesNacimiento > mesActual:
    edad = edad + 1
elif mesNacimiento == mesActual :
    edad = edad + 1    
print(f"Usted a cumplido: ",edad,"años")