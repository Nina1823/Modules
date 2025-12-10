#pgzero


WIDTH = 200 # Ancho de la ventana
HEIGHT = 200 # Altura de la ventana

TITLE = "Crystals" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Crea un personaje aquí
blue = Actor('blue', (20, 20))
red = Actor('red', (180, 20))
yellow = Actor('yellow', (180, 180))
green = Actor('green', (20, 180))

def draw():
    screen.fill('white')
    blue.draw()
    red.draw()
    yellow.draw()
    green.draw()

def update(dt):
    # Escribe tu código debajo
    blue.x = blue.x + 1
    blue.y = blue.y + 1
    red.x = red.x - 1
    red.y = red.y + 1  
    yellow.x = yellow.x - 1
    yellow.y = yellow.y - 1  
    green.x = green.x + 1
    green.y = green.y - 1  