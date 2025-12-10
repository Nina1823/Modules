#pgzero

WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 # # Altura de la ventana

TITLE = "Press the space bar" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (20, 20))
background = Actor("bg")

def draw():
    background.draw()
    alien.draw()
    
def update(dt):
    if keyboard.space:
	    animate(alien, tween='linear', duration=1, x = 280, y = 280)