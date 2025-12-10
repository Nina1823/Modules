#pgzero

# Ventana de juego hecha de celdas
cell = Actor('border')
size_w = 7 # Anchura del campo en celdas
size_h = 7 # Altura del campo en celdas
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo
    # j =  0, 1, 2, 3, 4, 5, 6 🟡🔵🟢
my_map = [[0, 0, 0, 0, 0, 0, 0], # i = 0 🟡🔵🟢
          [0, 1, 2, 1, 3, 1, 0], # i = 1 🟡🔵🟢
          [0, 1, 1, 2, 1, 1, 0], # i = 2 🟡🔵🟢
          [0, 3, 2, 1, 1, 3, 0], # i = 3 🟡🔵🟢
          [0, 1, 1, 1, 3, 1, 0], # i = 4 🟡🔵🟢
          [0, 1, 3, 1, 1, 2, 0], # i = 5 🟡🔵🟢
          [0, 0, 0, 0, 0, 0, 0]] # i = 6 🟡🔵🟢

def map_draw(): # 🟡🔵🟢
    for i in range(len(my_map)): # 🟡🔵🟢
        for j in range(len(my_map[0])): # 🟡🔵🟢
            cell.left = cell.width*j # 🟡🔵🟢
            cell.top = cell.height*i # 🟡🔵🟢
            cell.draw() # 🟡🔵🟢

def draw(): # 🟡🔵🟢
    map_draw() # 🟡🔵🟢