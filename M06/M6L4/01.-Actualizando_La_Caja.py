#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Alien Runner" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))

def draw():
    background.draw()
    alien.draw()
    box.draw()
    
def update(dt):
    # Movimiento de la caja
    if box.x > - 20: #🔴 (si la caja es mayor a  menos 20 venga hacia x en negativo y tenga un ángulo es decir a la derecha)
        box.x = box.x - 5 
        box.angle = box.angle + 5
    else: #🔴 ( de lo contrario apareza al otro lado)
        box.x = WIDTH + 20 #🔴