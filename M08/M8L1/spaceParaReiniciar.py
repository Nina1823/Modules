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
planets = [
    Actor("plan1", (random.randint(0, 600), -100)),
    Actor("plan2", (random.randint(0, 600), -100)),
    Actor("plan3", (random.randint(0, 600), -100))
]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("ship1", (100, 200))
type2 = Actor("ship2", (300, 200))
type3 = Actor("ship3", (500, 200))
count = 0

def fill():  # 🔴 Rellena enemigos y meteoritos
    global enemies, meteors
    enemies = []
    meteors = []
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        enemy = Actor("enemy", (x, y))
        enemy.speed = random.randint(2, 8)
        enemies.append(enemy)
    for i in range(5):
        x = random.randint(0, 600)
        y = random.randint(-450, -50)
        meteor = Actor("meteor", (x, y))
        meteor.speed = random.randint(2, 10)
        meteors.append(meteor)

fill()  # Inicializa listas

def draw():
    if mode == 'menu':
        space.draw()
        screen.draw.text('CHOOSE YOUR SHIP', center=(300, 100), color="white", fontsize=36)
        type1.draw()
        type2.draw()
        type3.draw()
    elif mode == 'game':
        space.draw()
        planets[0].draw()
        for m in meteors:
            m.draw()
        ship.draw()
        for e in enemies:
            e.draw()
        for b in bullets:
            b.draw()
        screen.draw.text(str(count), (10, 10), color="white")
    elif mode == 'end':
        space.draw()
        screen.draw.text("GAME OVER!", center=(300, 200), color="white", fontsize=48)
        screen.draw.text("Press SPACE to restart", center=(300, 280), color="white", fontsize=24)
        screen.draw.text(str(count), center=(300, 340), color="yellow", fontsize=48)

def on_mouse_move(pos):
    if mode == 'game':
        ship.pos = pos

def new_enemy():
    x = random.randint(0, 600)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

def enemy_ship():
    for e in enemies[:]:
        e.y += e.speed
        if e.y > HEIGHT + 50:
            enemies.remove(e)
            new_enemy()

def planet():
    if planets[0].y < HEIGHT + 100:
        planets[0].y += 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

def meteorites():
    for m in meteors:
        m.y += m.speed
        if m.y > HEIGHT:
            m.x = random.randint(0, 600)
            m.y = -20
            m.speed = random.randint(2, 10)

def collisions():
    global mode, count
    for e in enemies[:]:
        if ship.colliderect(e):
            mode = 'end'
            return
        for b in bullets[:]:
            if b.colliderect(e):
                count += 1
                enemies.remove(e)
                bullets.remove(b)
                new_enemy()
                break

def update(dt):
    global count, mode, enemies, planets, meteors, bullets
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        for b in bullets[:]:
            b.y -= 10
            if b.y < 0:
                bullets.remove(b)
    elif mode == 'end':
        if keyboard.space:
            restart_game()

def restart_game():  # 🔁 Reinicia todo el juego
    global mode, count, enemies, planets, meteors, bullets
    count = 0
    bullets = []
    planets = [
        Actor("plan1", (random.randint(0, 600), -100)),
        Actor("plan2", (random.randint(0, 600), -100)),
        Actor("plan3", (random.randint(0, 600), -100))
    ]
    fill()
    mode = 'menu'

def on_mouse_down(button, pos):
    global mode
    if mode == 'menu':
        if type1.collidepoint(pos):
            ship.image = "ship1"
            mode = 'game'
        elif type2.collidepoint(pos):
            ship.image = "ship2"
            mode = 'game'
        elif type3.collidepoint(pos):
            ship.image = "ship3"
            mode = 'game'
    elif mode == 'game' and button == mouse.LEFT:
        bullet = Actor("missiles")
        bullet.pos = ship.pos
        bullets.append(bullet)
