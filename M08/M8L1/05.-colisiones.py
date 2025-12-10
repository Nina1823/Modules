#pgzero
import random

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje al espacio"
FPS = 30

# Objetos y variables
ship = Actor("ship1", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("ship1", (100, 200))
type2 = Actor("ship2", (300, 200))
type3 = Actor("ship3", (500, 200))

# Elaboración de la lista de enemigos
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
# Elaboración de la lista de enemigos(meteoritos)
for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

# Elaboración
def draw():
    # Pantalla del menú de inicio
    if mode == 'menu':
        space.draw()
        screen.draw.text('ELIGE TU NAVE', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    # Modo de juego
    if mode == 'game':
        space.draw()
        planets[0].draw()
        # Atraer a los meteoritos
        for i in range(len(meteors)):
            meteors[i].draw()
        ship.draw()
        # Atraer a los enemigos
        for i in range(len(enemies)):
            enemies[i].draw()
        # Dibujando proyectiles hacia arriba   
        for i in range(len(bullets)):
            bullets[i].draw()
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

# Movimiento del planeta
def planet():
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

# Movimiento del meteorito
def meteorites():
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

# Colisiones
def collisions():
    global mode
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        # Colisiones de proyectiles
        for j in range(len(bullets)): # 🔴
            if bullets[j].colliderect(enemies[i]): # 🔴
                enemies.pop(i) # 🔴
                bullets.pop(j) # 🔴
                new_enemy() # 🔴
                break # 🔴

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        # Movimiento de proyectiles
        for i in range(len(bullets)):
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10
        
def on_mouse_down(button, pos):
    global mode, ship
    if mode == 'menu' and type1.collidepoint(pos):
        ship.image = "ship1"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        ship.image = "ship2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        ship.image = "ship3"
        mode = 'game'
    # Shooting    
    elif mode == 'game' and button == mouse.LEFT:
        bullet = Actor("missiles")
        bullet.pos = ship.pos
        bullets.append(bullet)