#pgzero

# Ventana de juego hecha de celdas
cell = Actor('border') #🔴 Cambiarlo
size_w = 7 # Anchura del campo en celdas
size_h = 7 # Altura del campo en celdas
WIDTH = cell.width * size_w  #🔴 posible error
HEIGHT = cell.height * size_h  #🔴 posible error

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo
    # j =  0, 1, 2, 3, 4, 5, 6 🔴
my_map = [[0, 0, 0, 0, 0, 0, 0], # i = 0 🔴
          [0, 1, 2, 1, 3, 1, 0], # i = 1 🔴
          [0, 1, 1, 2, 1, 1, 0], # i = 2 🔴
          [0, 3, 2, 1, 1, 3, 0], # i = 3 🔴
          [0, 1, 1, 1, 3, 1, 0], # i = 4 🔴
          [0, 1, 3, 1, 1, 2, 0], # i = 5 🔴
          [0, 0, 0, 0, 0, 0, 0]] # i = 6 🔴

def map_draw():
    # Esta función se encarga de dibujar todo el mapa en pantalla 🔴

    for i in range(len(my_map)):# Recorre las filas del mapa, i representa la fila actual 🔴
        for j in range(len(my_map[0])):# Recorre las columnas del mapa, j representa la columna actual 🔴

            # Calcula la posición horizontal de la celda
            # Se multiplica el ancho de la imagen por la columna
            cell.left = cell.width * j

            # Calcula la posición vertical de la celda
            # Se multiplica el alto de la imagen por la fila
            cell.top = cell.height * i

            # Dibuja la celda en la posición calculada
            cell.draw()


def draw(): # 🔴
    map_draw() # 🔴