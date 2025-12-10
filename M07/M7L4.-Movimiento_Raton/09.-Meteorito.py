#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje al espacio"
FPS = 30

# Objetos y variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []
meteors = [] #🔴🟢🔵🟡
mode = 'game' 

# Elaboración de la lista de enemigos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Añadir meteoritos a la lista
for i in range(5): #🔴🟢🔵🟡
    x = random.randint(0, 600) #🔴🟢🔵🟡
    y = random.randint(-450, -50) #🔴🟢🔵🟡
    meteor = Actor("meteor", (x, y)) #🔴🟢🔵🟡
    meteor.speed = random.randint(2, 10) #🔴🟢🔵🟡
    meteors.append(meteor)  #🔴🟢🔵🟡

# Elaboración
def draw():
    # Modo de juego
    if mode == 'game': 
        space.draw()
        # Elaboración de los meteoritos
        for i in range(len(meteors)): #🔴🟢🔵🟡
            meteors[i].draw() #🔴🟢🔵🟡
        ship.draw()
        # Atraer a los enemigos
        for i in range(len(enemies)):
            enemies[i].draw()
    # Ventana de finalización del juego    
    elif mode == 'end': 
        space.draw() 
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36) 
    
# Controles
def on_mouse_move(pos):
    ship.pos = pos

# Añadir nuevos enemigos a la lista
def new_enemy():
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Movimiento del enemigo
def enemy_ship():
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

# Movimiento del meteorito
def meteorites(): #🔴🟢🔵🟡
    for i in range(len(meteors)): #🔴🟢🔵🟡
        if meteors[i].y < 450: #🔴🟢🔵🟡
            meteors[i].y = meteors[i].y + meteors[i].speed #🔴🟢🔵🟡
        else: #🔴🟢🔵🟡
            meteors[i].x = random.randint(0, 600) #🔴🟢🔵🟡
            meteors[i].y = -20 #🔴🟢🔵🟡
            meteors[i].speed = random.randint(2, 10) #🔴🟢🔵🟡

# Colisiones
def collisions():
    global mode
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end' 

def update(dt):
    if mode == 'game': 
        enemy_ship()
        collisions()
        meteorites() #🔴🟢🔵🟡