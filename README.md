## Software de restaurante 

Dependiendo de la comida que pida el cliente, se le da el precio y la descripción de lo que pidió.

```python
from datetime import datetime
import random

class FacturaRestaurante:
    def __init__(self):
        self.menu = {
            'menú numero 1': {'precio': 31.000, 'plato': 'PARIHUELA PERUANA DE LA CASA.', 'descripcion': 'Parihuela tipo peruana con filete de bagre, \n calamar y camarones. Acompañada de arroz blanco.\n'},
            'menú numero 2': {'precio': 26.000, 'plato': 'CAZUELA LIMEÑA.','descripcion':'Puré amarillo relleno de aguacate, ceviche de salmón, \n aderezada y servida con granish de aceitunas negras y picadillo.\n'},
            'menú numero 3': {'precio': 23.500, 'plato': 'ARROZ CHAUFA.','descripcion':'Arroz al wok con vegetales, huevo en tortilla \n y pollo marinado, salsa de la casa. Acompañado de vegetales \n gruesos zukini verde y amarillo, zanahoria , brócoli y coliflor en salsa asiática.\n'},
            'menú numero 4': {'precio': 12.500, 'plato': 'ENSALADA.','descripcion':'Ensalada con tomate en cubos, hierbabuena, \n cebolla fina roja, pepino, cuscús, lechuga, uchuva, vinagreta.\n'},
            'menú numero 5': {'precio': 35.500, 'plato': 'LOMO SALTADO PERUANO.','descripcion':'Solomito brangus en lomos al wok con cebolla, \n tomate en julianas y perejil liso en salsa de la casa Acompañado de papa rústica\n'},
            'menú numero 6': {'precio': 29.500, 'plato': 'PASTA A LA CARBONARA.','descripcion':'Pasta artesanal con salsa Carbonara, \n con pollo Acompañada con pan de la casa.\n'},
            'menú numero 7': {'precio': 29.500, 'plato': 'PASTA A LA HUACAINA.','descripcion':'Pasta artesanal con salsa peruana huancaína, \n calamar, camarón, queso parmesano, y aceitunas negra. Acompañada con tostadas de la casa con ajo.\n'},
            'menú numero 8': {'precio': 29.500, 'plato': 'PASTA EN SALSA BLANCA.','descripcion':'Pasta artesanal en salsa blanca ahumada, \n con Salmón, aguacate en cubos y aceitunas negras. Acompañada con pan de la casa.\n'},
            'menú numero 9': {'precio': 27.500, 'plato': 'WRAP DE SOLOMITO DE RES.','descripcion':'Tortilla de harina de trigo, ligeramente asada, \n rellena de solomito de res, lechugas tomate en rodajas, aguacate, cebolla encurtida, \n salsa tzaziki Acompañada de papa rústica. Incluye, sopa, ensalada y jugo de fruta natural.\n'},
            'menú numero 10': {'precio': 18.500, 'plato': 'SANDWICH DE POLLO.','descripcion':'Pan artesanal, queso crema, lechuga, tomate, albahaca,\n espinaca, jamón o tocineta, pechuga de pollo a la plancha, salsa tártara; \n acompañado de papas a la francesa. Incluye jugo de fruta natural o gaseosa.\n'},
            'menú numero 11': {'precio': 10.500, 'plato': 'CREMAS.','descripcion':'TOMATE, CHAMPIÑONES, BROCOLI, CEBOLLA\n'},
        }
        self.items_seleccionados = []
        self.fecha = datetime.now()


    def mostrar_menu(self):
        print("Bienvenid@s a Restaurant ¡SABOR PERÚ!\n ")
        print("NUESTRO MENÚ:\n")
        for opcion, info in self.menu.items():
            print(f"- {opcion}: Valor: ${info['precio']} - Plato: {info['plato']} - Descripcion: {info['descripcion']}")

    def agregar_a_seleccion(self, opcion, cantidad):
        if opcion in self.menu:
            self.items_seleccionados.append((opcion, self.menu[opcion]['precio'], self.menu[opcion]['plato'], cantidad))
            print(f"{cantidad} {opcion} ¿Desea algo más?")
        else:
            print(f"'{opcion}' no está en el menú numero.")
#Crea la factura
    def generar_factura(self):
        print(" ")  
        print("RESTAURANT ¡SABOR PERÚ! \n ")
        print("NIT: 3336545212-21")   
        print("Direccion: Cra 100 Cll 001A-010 (Medellin).")
        print("Telefono: 604-50-50")
        print("Factura N° ",random.randint(1,10))  
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d \nHora: %H:%M:%S\n')}")
        total = 0
        print("Mesa N° ",random.randint(1,20))  
        for opcion, precio, plato, cantidad in self.items_seleccionados:
            print(f"{plato} \nCantidad: {cantidad} \nTotal: ${precio * cantidad}\n")
            total += precio * cantidad
        iva = total * 0.10
        total_con_iva = total + iva
        print(f"IVA (10%): ${iva}")
        print(f"Neto a Pagar (+ IVA): ${total_con_iva}\n")
        print("Lo atendio Nora.")
        print("Gracias por su Visita.\n")

# Crear una instancia de la clase FacturaRestaurante
factura = FacturaRestaurante()

# Mostrar el menú numero
factura.mostrar_menu()

# Permitir elegir opciones del menú numero
while True:
    opcion_elegida = input("¿Qué número del plato deseas (o 'x' para terminar): ")
    
    if opcion_elegida.lower() == 'x':
        break
    
    cantidad_elegida = int(input("¿Cuántos Menús? : "))
    factura.agregar_a_seleccion(f'menú numero {opcion_elegida}', cantidad_elegida)

# Generar la factura final
factura.generar_factura()

 ...








## Nomina para empresa

Calcule cuanto le vale a una empresa uno de sus empleado uno con 1 salario mínimo , nomina desde el punto de vista de la empresa y no del empleado.

```python
class Empleado:
    def __init__(self, sal_minimo, aux_transporte, salud, pension, arl,
                 cesantias, inte_cesantias, parafiscales, vacaciones, dotacion):
        self.sal_minimo = sal_minimo
        self.aux_transporte = aux_transporte
        self.salud = salud
        self.pension = pension
        self.arl = arl
        self.cesantias = cesantias
        self.inte_cesantias = inte_cesantias
        self.parafiscales = parafiscales
        self.vacaciones = vacaciones
        self.dotacion = dotacion

    def obligaciones(self):
        # Cálculos
        total_salario = self.sal_minimo * 1.16  # Aumento del 16% al salario mínimo
        total_transporte = self.aux_transporte * 1.20  # Aumento del 20% al auxilio de transporte
        total_salud = self.salud * 1.085  # Aumento del 8.5% al valor de salud
        total_pension = self.pension * 1.12  # Aumento del 12% al valor de pensión
        total_arl = self.arl * 1.00522  # Aumento del 0.522% al valor de ARL
        total_dotacion = self.dotacion * 1.025  # Aumento del 2.5% al valor de dotación


   
        total_obligacion = (
            total_salario + total_transporte + total_salud + total_pension +
            total_arl + self.cesantias + self.inte_cesantias +
            self.parafiscales + self.vacaciones + total_dotacion
        )

        return total_obligacion


empleado1 = Empleado(1160000, 140606, 98600, 139200, 6055, 108384, 1084, 104400, 48333, 29000)
total_obligaciones = empleado1.obligaciones()

print(f"Esto es lo que le cuesta 1 empleado a una empresa: ${total_obligaciones:,.2f}")

# ...



