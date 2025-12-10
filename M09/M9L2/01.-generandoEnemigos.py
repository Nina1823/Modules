#pgzero
import random # 🔴🟢🔵🟡

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

enemies = [] # 🔴🟢🔵🟡
for i in range(5):
    x = random.randint(1, 7) * cell.width # 🔴🟢🔵🟡
    y = random.randint(1, 7) * cell.height # 🔴🟢🔵🟡
    enemy = Actor("enemy", topleft = (x, y)) # 🔴🟢🔵🟡
    enemy.health = random.randint(10, 20) # 🔴🟢🔵🟡
    enemy.attack = random.randint(5, 10) # 🔴🟢🔵🟡
    enemies.append(enemy) # 🔴🟢🔵🟡

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
    screen.fill("#2f3542")
    map_draw()
    char.draw()
    screen.draw.text("HP:", center=(25, 475), color = 'white', fontsize = 20)
    screen.draw.text(char.health, center=(75, 475), color = 'white', fontsize = 20)
    screen.draw.text("AP:", center=(375, 475), color = 'white', fontsize = 20)
    screen.draw.text(char.attack, center=(425, 475), color = 'white', fontsize = 20)
    for i in range(len(enemies)): # 🔴🟢🔵🟡
        enemies[i].draw() # 🔴🟢🔵🟡

def on_key_down(key):
    if keyboard.right and char.x + cell.width < WIDTH - cell.width:
        char.x += cell.width
        char.image = 'stand'
    elif keyboard.left and char.x - cell.width > cell.width:
        char.x -= cell.width
        char.image = 'left'
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height*2:
        char.y += cell.height
    elif keyboard.up and char.y - cell.height > cell.height:
        char.y -= cell.height