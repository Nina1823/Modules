#pgzero
import random

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Corredor de Alienígenas" #  Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240)) 
fon = Actor("background") 
box = Actor('box', (550, 265)) 
bee = Actor('bee', (550, 175)) 
go = Actor("GO") 
# Variables
game_over = 0
count = 0
enemy = random.randint(1,2)

def boxes():
    global count
    global enemy#🔴🔴🔴🔴
    # Movimiento de la caja
    if box.x > -20:
        box.x = box.x - 5
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)#🔴🔴🔴🔴
        

def bees():
    global count
    global enemy#🔴🔴🔴🔴
    # Movimiento de la abeja
    if bee.x > -20:
        bee.x = bee.x - 5
    else:
        bee.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)#🔴🔴🔴🔴

def draw():
    fon.draw()
    alien.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    if game_over == 1:
        go.draw()
        screen.draw.text('Нажмите Enter', pos=(170, 150), color="white", fontsize = 36)
    if enemy == 1:#🔴🔴🔴🔴
        box.draw()#🔴🔴🔴🔴
    else:#🔴🔴🔴🔴
        bee.draw()#🔴🔴🔴🔴
    
def update(dt):
    # Variables
    global count
    global game_over
    global enemy    #🔴🔴🔴🔴
    #  Llamando funciones
    if enemy == 1:#🔴🔴🔴🔴
        boxes()#🔴🔴🔴🔴
    elif enemy == 2:#🔴🔴🔴🔴
        bees()#🔴🔴🔴🔴
    
    # Controles
    if keyboard.left or keyboard.a and alien.x > 20:
        alien.x = alien.x - 5
        alien.image = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580:
        alien.x = alien.x + 5
        alien.image = 'right'
    elif keyboard.down or keyboard.s:
        alien.image = 'duck'
        alien.y = 250
    else:
        alien.image = 'alien'
        if alien.y > 240:
            alien.y = 240
    
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        alien.pos = (50, 240)
        box.pos =(550, 265)
        bee.pos = (550, 175)
    
    # Colisión
    if alien.colliderect(box) or alien.colliderect(bee):
        game_over = 1

# Salto       
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)