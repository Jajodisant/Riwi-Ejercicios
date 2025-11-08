
pruebaTecnica = float(input("Ingresa la primera nota de 0 a 5: \n"))

pruebaLogica = float(input("Ingresa la primera nota de 0 a 5: \n"))

notaFinal = (pruebaTecnica *  0.7) + (pruebaLogica * 0.3)

if notaFinal >= 2 and notaFinal <= 3:
    print("En revision con nota de", notaFinal)
elif notaFinal >= 3:
    print("Haz Ganado con ", notaFinal)
else:
    print("Reprobado con" , notaFinal)
