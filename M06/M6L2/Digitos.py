# Pidiendo al usuario que ingrese un número
number = input("Ingresa un número: ")

# Creando un contador para los dígitos divisibles por tres
count = 0

# La entrada devuelve una cadena; necesitamos iterar a través de cada carácter de esta cadena utilizando un bucle for
for digit in number:
    # Verificando si el dígito es divisible por tres
    if int(digit) % 3 == 0:
        count += 1

# Mostrando los resultados
print("Número de dígitos divisibles por tres: ", count)
