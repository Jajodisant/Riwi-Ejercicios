""" 1. Restaurante “Buen Sabor” – Cálculo de propina
Como mesero, quiero una función calcular_propina(total_cuenta) que reciba el valor total de la cuenta y 
calcule la propina del 10%.
Si el total es mayor de $100.000, aplicar el 15%.
El programa debe mostrar el total final a pagar. """



def propinas(self):
    cuenta = self
    if cuenta > 100000:
        propina = cuenta * 0.15
        total= cuenta + propina
        print(f"el valor de la cuenta es: {total} y la propina es {propina}")
    else:
        propina = cuenta * 0.10
        total= cuenta + propina
        print(f"el valor de la cuenta es: {total} y la propina es {propina}")


valor = int(input("Ingrese el valor de la cuenta: "))

propinas(valor)
