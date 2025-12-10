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
mode = 'game' #🔴🟢🔵🟡

# Elaboración de la lista de enemigos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Elaboración
def draw():
    # Modo de juego
    if mode == 'game': #🔴🟢🔵🟡
        space.draw()
        ship.draw()
        # Atraer a los enemigos
        for i in range(len(enemies)):
            enemies[i].draw()
    # Ventana de finalización del juego    
    elif mode == 'end': #🔴🟢🔵🟡
        space.draw() #🔴🟢🔵🟡
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36) #🔴🟢🔵🟡
    
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

# Colisiones
def collisions():
    global mode #🔴🟢🔵🟡
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end' #🔴🟢🔵🟡

def update(dt):
    if mode == 'game': #🔴🟢🔵🟡
        enemy_ship()
        collisions()