#"""Función para calcular la diferencia entre dos números"""
def calculate_difference(a, b):
    return a - b

# Pidiendo al usuario que ingrese los números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Llamando a la función para calcular la diferencia y mostrando el resultado
difference = calculate_difference(number1, number2)
print("La diferencia entre", number1, "y", number2, "es", difference)