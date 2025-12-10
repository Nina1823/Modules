#pgzero
import random, time

WIDTH = 600
HEIGHT = 400
TITLE = "Escape & Monedas - Niveles Infinitos"

# Actores principales
hero = Actor("hero", (300, 200), size=(45,45))
companion = Actor("enemy", (400, 300), size=(45,45))

enemies = []
coins = []

score = 0
level = 1
start_time = time.time()
last_enemy_time = start_time
game_over = False
double_points = False

def reset_game():
    global score, level, enemies, coins, start_time, last_enemy_time, double_points, game_over
    score = 0
    level = 1
    enemies = []
    coins = []
    start_time = time.time()
    last_enemy_time = start_time
    double_points = True
    game_over = False

def spawn_enemy():
    x = random.choice([0, WIDTH])
    y = random.randint(0, HEIGHT)
    enemy = Actor("enemy", (x, y))
    enemies.append(enemy)

def spawn_coin():
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    coin = Actor("coin", (x, y))
    coins.append(coin)

def update_level():
    global level
    if score >= 400:
        level = 5
    elif score >= 300:
        level = 4
    elif score >= 200:
        level = 3
    elif score >= 100:
        level = 2
    else:
        level = 1

def update(dt=0):
    global score, last_enemy_time, game_over
    if game_over:
        return

    now = time.time()
    update_level()

    if score >= 500:
        reset_game()

    # Héroe sigue el ratón
    hero.pos = pygame.mouse.get_pos()  

    # Aparición de enemigos
    if now - last_enemy_time >= 10:
        if int(now - start_time) % 50 == 0:
            spawn_enemy()
            spawn_enemy()
        else:
            spawn_enemy()
        last_enemy_time = now

    # Aparición aleatoria de monedas
    if random.random() < 0.02:
        spawn_coin()

    # Movimiento enemigos y colisiones
    for e in enemies:
        dx = hero.x - e.x
        dy = hero.y - e.y
        dist = max(1, (dx**2 + dy**2)**0.5)
        speed_e = 1.5 + level * 0.3
        e.x += dx/dist * speed_e
        e.y += dy/dist * speed_e
        if e.colliderect(hero):
            game_over = True

    # Recolección de monedas
    for c in coins[]:
        if c.colliderect(hero):
            coins.remove(c)
            score += 2 if double_points else 1

def draw():
    screen.clear()
    screen.blit("background", (0,0))

    # Dibujar actores
    hero.draw()
    companion.draw()

    for e in enemies:
        e.draw()
    for c in coins:
        c.draw()

    # Texto
    screen.draw.text("Puntos: " + str(score), (10, 10), color="white", fontsize=40)
    screen.draw.text("Nivel: " + str(level), (10, 50), color="yellow", fontsize=40)
    if double_points:
        screen.draw.text("x2 Puntos Activo", (10, 90), color="cyan", fontsize=30)

    if game_over:
        screen.draw.text("GAME OVER", center=(WIDTH//2, HEIGHT//2), color="red", fontsize=80)