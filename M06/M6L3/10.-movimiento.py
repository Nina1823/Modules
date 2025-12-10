#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Alien Runner" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

#crea un personaje aquí
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))

def draw():
    background.draw()
    alien.draw()
    box.draw()
    
def update(dt):
    box.x = box.x - 5
    box.angle = box.angle + 5