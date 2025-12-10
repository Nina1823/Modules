#pgzero
#TRASLADAR LA LOGICA DE UPDATE Y COLOCARLO EN enemies() y llamar la fn en update()
WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Función para el movimiento de los enemigos" # Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('stand', (50, 240)) 
background = Actor("background") 
enemy = Actor('yellow', (250, 270)) 

def draw():
    background.draw()
    alien.draw()
    enemy.draw()
    
def enemies(): # Movimiento del enemigo #🔴🔴🔴🔴
    if enemy.x > -20: #🔴🔴🔴🔴
        enemy.x = enemy.x - 10 #🔴🔴🔴🔴
        enemy.angle = enemy.angle + 10 #🔴🔴🔴🔴
    else:#🔴🔴🔴🔴
        enemy.x = WIDTH + 20 #🔴🔴🔴🔴

def update(dt):
    enemies() # Llamando a la función que esta en la linea 18 #🔴🔴🔴🔴
    # Controles
    if keyboard.left and alien.x > 20: 
        alien.x = alien.x - 5

    elif keyboard.right and alien.x < 280: 
        alien.x = alien.x + 5