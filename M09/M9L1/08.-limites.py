#pgzero

# Ventana de juego
cell = Actor('border')
cell1 = Actor('floor')
cell2 = Actor("crack")
cell3 = Actor("bones")
size_w = 7 # Anchura del campo en celdas
size_h = 7 # Altura del campo en celdas
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
          [0, 0, 0, 0, 0, 0, 0]]
          
char = Actor('stand')
char.top = cell.height
char.left = cell.width
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
    map_draw()
    char.draw()
    screen.draw.text(char.health, center=(325, 10), color = 'white', fontsize = 16)
    screen.draw.text(char.attack, center=(325, 25), color = 'white', fontsize = 16)

# Función que se ejecuta cuando el jugador presiona una tecla
def on_key_down(key):
    # Si se presiona la flecha derecha y el personaje no sale del borde derecho
    if keyboard.right and char.x + cell.width < WIDTH - cell.width:
        # Mueve el personaje una celda hacia la derecha
        char.x += cell.width
        # Cambia la imagen del personaje para que mire hacia adelante
        char.image = 'stand'

    # Si se presiona la flecha izquierda y el personaje no sale del borde izquierdo
    elif keyboard.left and char.x - cell.width > cell.width:
        # Mueve el personaje una celda hacia la izquierda
        char.x -= cell.width
        # Cambia la imagen del personaje para que mire hacia la izquierda
        char.image = 'left'

    # Si se presiona la flecha abajo y el personaje no sale del borde inferior
    elif keyboard.down and char.y + cell.height < HEIGHT - cell.height:
        # Mueve el personaje una celda hacia abajo
        char.y += cell.height

    # Si se presiona la flecha arriba y el personaje no sale del borde superior
    elif keyboard.up and char.y - cell.height > cell.height:
        # Mueve el personaje una celda hacia arriba
        char.y -= cell.height
