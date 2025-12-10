# Los enemigos vienen y se mueven


#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje al espacio 🚀"
FPS = 30

# Objetos y variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = [] #🔴🟢🔵🟡

# Elaboración de la lista de enemigos
for i in range(5): #🔴🟢🔵🟡
    x = random.randint(40, WIDTH-40) #🔴🟢🔵🟡
    y = random.randint(-450, -50) #🔴🟢🔵🟡
    enemy = Actor("enemy", (x, y)) #🔴🟢🔵🟡
    enemy.speed = random.randint(2, 8) #🔴🟢🔵🟡
    enemies.append(enemy) #🔴🟢🔵🟡

# Elaboración
def draw():
    space.draw()
    ship.draw()
    for i in range(len(enemies)): #🔴🟢🔵🟡
        enemies[i].draw() #🔴🟢🔵🟡
    
# Controles
def on_mouse_move(pos):
    ship.pos = pos

# Movimiento del enemigo
def enemy_ship(): #🔴🟢🔵🟡
    for i in range(len(enemies)): #🔴🟢🔵🟡
        if enemies[i].y < 650: #🔴🟢🔵🟡
            enemies[i].y = enemies[i].y + enemies[i].speed #🔴🟢🔵🟡

def update(dt): #🔴🟢🔵🟡
    enemy_ship() #🔴🟢🔵🟡