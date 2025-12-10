#pgzero

# Ventana de juego hecha de celdas
cell = Actor('border')
size_w = 7 # Anchura del campo en celdas
size_h = 7 # Altura del campo en celdas
WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo
my_map = [[0, 0, 0, 0, 0, 0, 0], # 🟡🔵🟢
          [0, 1, 2, 1, 3, 1, 0], # 🟡🔵🟢
          [0, 1, 1, 2, 1, 1, 0], # 🟡🔵🟢
          [0, 3, 2, 1, 1, 3, 0], # 🟡🔵🟢
          [0, 1, 1, 1, 3, 1, 0], # 🟡🔵🟢
          [0, 1, 3, 1, 1, 2, 0], # 🟡🔵🟢
          [0, 0, 0, 0, 0, 0, 0]] # 🟡🔵🟢