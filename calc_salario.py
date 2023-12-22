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
