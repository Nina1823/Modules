#pgzero
import random 

# Ventana de juego
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("crack")
cell3 = Actor("bones")
size_w = 9 # Anchura del campo en celdas
size_h = 10 # Altura del campo en celdas
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego 
FPS = 30 # Número de fotogramas por segundo
my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Fila de poder de ataque y salud

# Protagonista
char = Actor('stand')
char.top = cell.height
char.left = cell.width
char.health = 100
char.attack = 5
attack_message = "" 
mode = "game"
win = 0

enemies = [] 
hearts = [] 
swords = [] 
for i in range(7):
    x = random.randint(1, 7) * cell.width 
    y = random.randint(1, 7) * cell.height 
    enemy = Actor("enemy", topleft = (x, y)) 
    enemy.health = random.randint(10, 20) 
    enemy.attack = random.randint(5, 10) 
    enemy.bonus = random.randint(0, 2) 
    enemies.append(enemy) 

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()
            elif my_map[i][j] == 1:
                cell1.left = cell.width*j
                cell1.top = cell.height*i
                cell1.draw()
            elif my_map[i][j] == 2:
                cell2.left = cell.width*j
                cell2.top = cell.height*i
                cell2.draw()  
            elif my_map[i][j] == 3:
                cell3.left = cell.width*j
                cell3.top = cell.height*i
                cell3.draw() 

def draw():
    if mode == "game":
      screen.fill("#2f3542")
      map_draw()
      char.draw()
      screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
      screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
      screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
      screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
      for i in range(len(enemies)): 
          enemies[i].draw() 
      if attack_message:
          screen.draw.text(attack_message, center=(150, 475), color="red", fontsize=15) 
      for i in range(len(hearts)): 
          hearts[i].draw() 
      for i in range(len(swords)): 
          swords[i].draw() 

    elif mode == "end":
        screen.fill("black")
        if win == 1:
          screen.draw.text("¡Has ganado!", center=(WIDTH//2, HEIGHT//2), color="white", fontsize=60)
        else:
            screen.draw.text("¡Has perdido!", center=(WIDTH//2, HEIGHT//2), color="white", fontsize=60)

def on_key_down(key):
    global attack_message 
    if (keyboard.right or keyboard.d) and char.x + cell.width < WIDTH - cell.width: #🔴🟢🔵🟡
        char.x += cell.width
        char.image = 'stand'
    elif (keyboard.left or keyboard.a) and char.x - cell.width > cell.width: #🔴🟢🔵🟡
        char.x -= cell.width
        char.image = 'left'
    elif (keyboard.down  or keyboard.s) and char.y + cell.height < HEIGHT - cell.height*2: #🔴🟢🔵🟡
        char.y += cell.height
    elif (keyboard.up  or keyboard.w) and char.y - cell.height > cell.height: #🔴🟢🔵🟡
        char.y -= cell.height

    old_x = char.x 
    old_y = char.y 
    enemy_index = char.collidelist(enemies) 
    if enemy_index != -1: 
        enemy = enemies[enemy_index] 
        enemy.health -= char.attack 
        char.health -= enemy.attack 
        attack_message = "¡Enemigo N°: " + str(enemy_index + 1) + " Ataque: " + str(enemy.attack) + "!"
        char.x = old_x 
        char.y = old_y 
        if enemy.health <= 0: 
            enemies.pop(enemy_index) 
            if enemy.bonus == 1: 
                heart = Actor('heart') 
                heart.pos = enemy.pos 
                hearts.append(heart) 
            elif enemy.bonus == 2: 
                sword = Actor('sword') 
                sword.pos = enemy.pos 
                swords.append(sword) 

def victory():
    global mode, win
    if enemies == [] and char.health > 0:
        mode = "end"
        win = 1
    elif char.health <= 0:
        mode = "end"
        win = -1
                
def update(dt): 
    victory()
    for i in range(len(hearts)): 
        if char.colliderect(hearts[i]):  
            char.health += 5  
            hearts.pop(i)  
            break  
        
    for i in range(len(swords)):
        if char.colliderect(swords[i]):
            def del_swords():
                if swords[i] in swords:
                    swords.pop(i)
            animate(swords[i], tween='bounce_end', duration=0.5, y=swords[i].y-10, on_finished=del_swords)
            char.attack += 5
            break        