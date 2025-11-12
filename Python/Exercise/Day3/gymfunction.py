""" 
2. Gimnasio “Level Up” – Control de repeticiones
Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar 
las repeticiones del 1 al número indicado.
Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”. """


def repeticiones (self):
    for i in range(self):
        print(f"repeicion {i}")
        i+=1
    if( i % 2 ==0):
         print("Excelente forma")
    else:
        print("Manten el ritmo")

series= int(input(" ingrese las repeticiones: "))

repeticiones(series)