#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje espacial"
FPS = 30

# Objetos y variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = []

# Elaboración de la lista de enemigos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

# Elaboración
def draw():
    space.draw()
    ship.draw()
    # Drawing enemies up
    for i in range(len(enemies)):
        enemies[i].draw()
    
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
def collisions(): #🔴🟢🔵🟡
    for i in range(len(enemies)): #🔴🟢🔵🟡
        if ship.colliderect(enemies[i]): #🔴🟢🔵🟡
            exit() #🔴🟢🔵🟡

def update(dt):
    enemy_ship()
    collisions() #🔴🟢🔵🟡