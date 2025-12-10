#pgzero

WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Controls example" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (150, 150))
background = Actor("bg")

def draw():
    background.draw()
    alien.draw()
    
def update(dt):
    if keyboard.left:
	    # Qué ocurre cuando se pulsa la flecha de la izquierda
	    alien.x = alien.x - 5