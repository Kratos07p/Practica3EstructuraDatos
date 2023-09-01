def obtenerMes(numMes):
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    if 1 <= numMes <= 12:
        nombreMes = meses[numMes - 1]
        return nombreMes
    else:
        return "Un Mes No Existente"

numero = int(input("Ingrese un número entre 1 y 12: "))
nombreDelMes = obtenerMes(numero)

print(f"El número {numero} corresponde a: {nombreDelMes}.")