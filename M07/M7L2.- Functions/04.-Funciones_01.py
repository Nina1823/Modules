#Cambiar el nivel de dificultad del juego con un aumento de velocidad incial de 5 e ir incrementando por cada enemigo

#pgzero
import random

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Corredor de Alienígenas" #  Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))
new_image = 'alien' #Seguimiento de la imagen actual
bee = Actor('bee', (550, 175))
go = Actor("GO")
# Variables
game_over = 0
count = 0
enemy = random.randint(1,2)
speed = 5#🔴🔴🔴🔴

def boxes():
    global count
    global enemy
    global speed#🔴🔴🔴🔴
    # Movimiento de la caja
    if box.x > -20:
        box.x = box.x - speed#🔴🔴🔴🔴
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1#🔴🔴🔴🔴
        
def bees():
    global count
    global enemy
    global speed#🔴🔴🔴🔴
    # Movimiento de la abeja
    if bee.x > -20:
        bee.x = bee.x - speed#🔴🔴🔴🔴
    else:
        bee.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1#🔴🔴🔴🔴

def draw():
    background.draw()
    alien.draw()
    if enemy == 1:
        box.draw()
    else:
        bee.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    if game_over == 1:
        go.draw()
        screen.draw.text('Press Enter', pos=(170, 150), color= "white", fontsize = 36)

    
def update(dt):
    # Variables
    global new_image
    global count
    global game_over
    global speed#🔴🔴🔴🔴
    
    # Llamando una función
    if enemy == 1:
        boxes()
    else:
        bees()
        
    # Controles
    if keyboard.left or keyboard.a and alien.x > 20:
        alien.x = alien.x - 5
        if new_image != 'left':
            alien.image = 'left'
            new_image = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580:
        alien.x = alien.x + 5
        if new_image != 'right':
            alien.image = 'right'
            new_image = 'right'
    elif keyboard.down or keyboard.s:
        if new_image != 'duck':
            alien.image = 'duck'
            new_image = 'duck'
            alien.y = 250
    else:
        if alien.y > 240 and new_image == 'duck':
            alien.image = 'alien'
            new_image = 'alien'
            alien.y = 240
    
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        alien.pos = (50, 240)
        box.pos = (550, 265)
        bee.pos = (550, 175)
        speed = 5#🔴🔴🔴🔴
    
    # Colisión
    if alien.colliderect(box) or alien.colliderect(bee):
        game_over = 1

# Salto        
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)
