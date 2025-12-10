import turtle

# Función para dibujar un cuadrado con un lado de longitud dada
def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

# Creando un objeto turtle
t = turtle.Turtle()

# Configurando la velocidad del dibujo
t.speed(1)  # La velocidad varía de 1 (más lenta) a 10 (más rápida)

# Solicitando al usuario los tamaños de tres cuadrados
sizes = []
for i in range(1, 4):
    size = int(input("Introduce la longitud del lado del cuadrado " + str(i) + ": "))
    sizes.append(size)

# Dibuja tres cuadrados con diferentes tamaños
for size in sizes:
    draw_square(size)

# Completa el proceso de dibujo con turtle
turtle.done()
