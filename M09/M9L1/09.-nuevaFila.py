#pgzero

# Ventana de juego
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("crack")
cell3 = Actor("bones")
size_w = 7 # Anchura del campo en celdas # 🟢🔵🟡
size_h = 8 # Altura del campo en celdas # 🟢🔵🟡
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 #  Número de fotogramas por segundo
my_map = [[0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 2, 1, 3, 1, 0], 
          [0, 1, 1, 2, 1, 1, 0], 
          [0, 3, 2, 1, 1, 3, 0], 
          [0, 1, 1, 1, 3, 1, 0], 
          [0, 1, 3, 1, 1, 2, 0], 
          [0, 0, 0, 0, 0, 0, 0], 
          [-1, -1, -1, -1, -1, -1, -1]] # 🟢🔵🟡

char = Actor('stand')
char.health = 100
char.attack = 5

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
    screen.fill("#2f3542") # 🟢🔵🟡
    map_draw()
    char.draw()
    screen.draw.text("HP:", center=(25, 375), color = 'white', fontsize = 20) # 🟢🔵🟡
    screen.draw.text(char.health, center=(75, 375), color = 'white', fontsize = 20) # 🟢🔵🟡
    screen.draw.text("AP:", center=(275, 375), color = 'white', fontsize = 20) # 🟢🔵🟡
    screen.draw.text(char.attack, center=(325, 375), color = 'white', fontsize = 20) # 🟢🔵🟡

def on_key_down(key):
    if keyboard.right and char.x + cell.width < WIDTH - cell.width: 
        char.x += cell.width
        char.image = 'stand'
    elif keyboard.left and char.x - cell.width > cell.width: 
        char.x -= cell.width
        char.image = 'left'
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height: 
        char.y += cell.height
    elif keyboard.up and char.y - cell.height > cell.height: 
        char.y -= cell.height