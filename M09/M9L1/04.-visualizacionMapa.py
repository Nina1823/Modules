#pgzero

# Ventana de juego
cell = Actor('border')
cell1 = Actor('floor') # 🟡🔵🟢
cell2 = Actor("crack") # 🟡🔵🟢
cell3 = Actor("bones") # 🟡🔵🟢
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
          

def map_draw():  
    for i in range(len(my_map)):  # Recorre las filas del mapa, i representa la fila actual  #🔴    
        for j in range(len(my_map[0])): # Recorre las columnas del mapa, j representa la columna actual  #🔴
            if my_map[i][j] == 0:  # Si el número del mapa es 0, es una pared  #🔴
                cell.left = cell.width * j # Coloca la imagen de la pared en la posición horizontal correcta
                cell.top = cell.height * i  # Coloca la imagen de la pared en la posición vertical correcta
                cell.draw()  # Dibuja la pared en pantalla
            elif my_map[i][j] == 1:  # Si el número del mapa es 1, es suelo
                cell1.left = cell.width * j  # Coloca la imagen del suelo en la columna correcta
                cell1.top = cell.height * i  # Coloca la imagen del suelo en la fila correcta
                cell1.draw()  # Dibuja el suelo en pantalla
            elif my_map[i][j] == 2:  # Si el número del mapa es 2, es una grieta
                cell2.left = cell.width * j   # Coloca la imagen de la grieta en la columna correcta
                cell2.top = cell.height * i   # Coloca la imagen de la grieta en la fila correcta
                cell2.draw()  # Dibuja la grieta en pantalla
            elif my_map[i][j] == 3:  # Si el número del mapa es 3, son huesos
                cell3.left = cell.width * j  # Coloca la imagen de los huesos en la columna correcta
                cell3.top = cell.height * i  # Coloca la imagen de los huesos en la fila correcta
                cell3.draw()    # Dibuja los huesos en pantalla

def draw():
    map_draw()