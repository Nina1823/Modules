#pgzero

# Ventana de juego hecha de celdas
cell = Actor('border') # 🟡🔵🟢 👁️ quite el cell = 50 y poner es el Actor
size_w = 5 # Anchura del campo en celdas
size_h = 5 # Altura del campo en celdas
WIDTH = cell.width * size_w # 🟡🔵🟢 se agrega a la cell el ..width
HEIGHT = cell.height * size_h # 🟡🔵🟢 se agrega a la cell el ..height

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo