#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Título del juego" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo


#crea un personaje aquí
detail = Actor('detail', (150, 150))

def draw():
    screen.fill('white')
    detail.draw()

def update(dt):
    detail.angle = detail.angle - 10