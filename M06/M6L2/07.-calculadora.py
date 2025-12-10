def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            return "Error: ¡División por cero!"
    else:
        return "Error: ¡Operación no soportada!"

# Solicitar al usuario los números y el tipo de operación
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
operation = input("Especifica la operación que deseas realizar (+, -, *, /): ")

# Llamando a la función 'calculate' y mostrando el resultado
result = calculate(a, b, operation)
print("Resultado:", result)
