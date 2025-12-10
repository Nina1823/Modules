#encontrar los 5 bugsss, al terminar ocpiar el codigo
#pgzero
import random

WIDTH = 600
HEIGHT = 300 

player = Actor('hero', (400, 300), size=(70, 70)) #Cambiar hero1 por hero (1) 🟢🟢🟢🟢🔴🔴🔴🔴🔴

star = Actor('star', size=(30, 30))
star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

enemies = []
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30)) # El tamaño no es 300 sino 30 (2) 🟢🟢🟢🟢🔴🔴🔴🔴🔴
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)
enemy = Actor('enemy', size=(30, 30))
enemy.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)
enemy.speed_x = random.choice([2, -2])
enemy.speed_y = random.choice([2, -2])
enemies.append(enemy)

background = Actor('background')

score = 0
game_over = False # Debería estar en False para que el juego comience no en true (3) 🟢🟢🟢🟢🔴🔴🔴🔴🔴

def draw():
    screen.clear()
    fon.draw()
    if not game_over:
        player.draw()
        star.draw()
        for enemy in enemies:
            enemy.draw()
        screen.draw.text(score, (10, 10), color='white')
    else:
        screen.draw.text('You lost! Press R to restart', center=(WIDTH // 2, HEIGHT // 2), fontsize=30, color='red')

def update(dt):
    global score, game_over

    if game_over:
        if keyboard.r: # Reiniciar el juego pero dice que con enter y no con r (4) 🟢🟢🟢🟢🔴🔴🔴🔴🔴
            restart_game()
        return

    if keyboard.left:
        if player.left > 0:
            player.x -= 10
    if keyboard.right:
        if player.right < WIDTH:
            player.x += 10
    if keyboard.up:
        if player.top > 0:
            player.y -= 10
    if keyboard.down:
        if player.bottom < HEIGHT:
            player.y += 10

    if player.colliderect(star):
        score += 1 # Debe aumentar y no disminuir (5) 🟢🟢🟢🟢🔴🔴🔴🔴🔴
        star.pos = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

    for enemy in enemies:
        enemy.x += enemy.speed_x
        enemy.y += enemy.speed_y

        if enemy.left < 0:
            enemy.speed_x = -enemy.speed_x
        if enemy.right > WIDTH:
            enemy.speed_x = -enemy.speed_x
        if enemy.top < 0:
            enemy.speed_y = -enemy.speed_y
        if enemy.bottom > HEIGHT:
            enemy.speed_y = -enemy.speed_y

        if player.colliderect(enemy):
            game_over = True

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