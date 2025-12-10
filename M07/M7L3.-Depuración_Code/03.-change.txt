#pgzero
import random

# Ajustar del tamaño de la ventana
WIDTH = 600
HEIGHT = 300

# Inicializando el jugador
player = Actor('hero', (400, 300), size=(70, 70))

# Inicializando la estrella
star = Actor('star', size=(30, 30))
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# Inicializando los enemigos
enemies = []
for i in range(7):
    enemy = Actor('enemy', size=(30, 30))
    enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    enemy.speed_x = random.choice([2, -2])  # Enemy speed across the X-axis
    enemy.speed_y = random.choice([2, -2])  # Enemy speed across the Y-axis
    enemies.append(enemy)

# Inicializando el fondo
background = Actor('background')

# Declarando la variable de puntuación y el libro de fin de juego
score = 0
game_over = False

def draw():
    screen.clear()
    background.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(score, (10, 10), color='white')
    else:
        screen.draw.text('¡Perdiste! Presiona R para reiniciar', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')

def update(dt):
    global score, game_over

    if game_over:
        if keyboard.r:
            restart_game()
        return

    # Player controls
    if keyboard.left and player.left > 0:
        player.x -= 10
    if keyboard.right and player.right < WIDTH:
        player.x += 10
    if keyboard.up and player.top > 0:
        player.y -= 10
    if keyboard.down and player.bottom < HEIGHT:
        player.y += 10

   # Comprobación de colisión de estrellas
    if player.colliderect(star): #aca se cambia a star para game over
        game_over = True

    # Mover enemigos y comprobar si hay colisiones
    for enemy in enemies:
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y

        # Cambiar la dirección de los enemigos al llegar al borde de la pantalla.
        if enemy.left < 0 or enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0 or enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y

        # Comprobación de colisión enemiga
        if player.colliderect(enemy):
            score += 1
            enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
            

def restart_game():
    global score, game_over
    player.pos = 400, 300
    star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
    for enemy in enemies:
        enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
        enemy.speed_x = random.choice([2, -2])
        enemy.speed_y = random.choice([2, -2])
    score = 0
    game_over = False