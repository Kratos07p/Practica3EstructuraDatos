notas = []

for i in range(5):
    while True:
        try:
            nota = float(input(f"Por favor ingrese la nota N°{i + 1}: "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota no valida, por favor ingrese una nota correcta entre [0 y 10].")
        except ValueError:
            print("No se ha ingresado un valor numerico, ingrese nuevamente.")

    notas.append(nota)

print("Notas obtenidas:")
for i, nota in enumerate(notas, start=1):
    print(f"Nota N°{i}: {nota}")

notaMedia = sum(notas) / len(notas)
notaMaxima = max(notas)
notaMinima = min(notas)

print("Nota media:", notaMedia)
print("Nota más alta:", notaMaxima)
print("Nota menor:", notaMinima)