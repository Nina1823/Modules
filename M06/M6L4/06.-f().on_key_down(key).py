#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Alien Runner" # Título para la ventana de juego
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
    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        
    # Controles
    if keyboard.left and alien.x > 20:
        alien.x = alien.x - 5
    elif keyboard.right and alien.x < 580:
        alien.x = alien.x + 5

def on_key_down(key): #🔴
    # Salto
    if keyboard.space:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)