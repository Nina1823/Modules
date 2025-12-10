# En cuanto nuestro enemigo pase por la ventana de juego, lo eliminaremos de la lista y añadiremos uno nuevo.
# Para generar nuevos enemigos, crearemos una función new_enemy().

#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje al espacio 🚀"
FPS = 30

# Objetos y variables
ship = Actor("ship", (300, 400))
space = Actor("space")
enemies = [] 

# Elaboración de la lista de enemigos
for i in range(5): 
    x = random.randint(40, WIDTH-40) 
    y = random.randint(-450, -50) 
    enemy = Actor("enemy", (x, y)) 
    enemy.speed = random.randint(2, 8) 
    enemies.append(enemy) 

# Elaboración
def draw():
    space.draw()
    ship.draw()
     # Dibujando los enemigos
    for i in range(len(enemies)): 
        enemies[i].draw() 
    
# Controles
def on_mouse_move(pos):
    ship.pos = pos

# Añadir nuevos enemigos a la lista
def new_enemy(): #🔴🟢🔵🟡
    x = random.randint(0, 400) #🔴🟢🔵🟡
    y = -50 #🔴🟢🔵🟡
    enemy = Actor("enemy", (x, y)) #🔴🟢🔵🟡
    enemy.speed = random.randint(2, 8) #🔴🟢🔵🟡
    enemies.append(enemy) #🔴🟢🔵🟡
    
# Movimiento del enemigo
def enemy_ship(): 
    for i in range(len(enemies)):
        if enemies[i].y < 650: 
            enemies[i].y = enemies[i].y + enemies[i].speed 
        else: #🔴🟢🔵🟡
            enemies.pop(i) #🔴🟢🔵🟡
            new_enemy() #🔴🟢🔵🟡
            

def update(dt): 
    enemy_ship() 