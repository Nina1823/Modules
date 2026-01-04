# my_map es un mapa del juego, hecho como una tabla (matriz).
# Cada fila es una línea del mapa
# Cada número es una celda
# Cada celda indica qué hay en ese lugar

# 👉 El juego lee los números y dibuja imágenes según el valor.
# 🟨 0 → Pared / Borde

# No se puede caminar por ahí
# Rodea la mazmorra
# Evita que el jugador salga del mapa
# 🧱 Es como un muro

# 🟦 1 → Suelo
# El personaje sí puede caminar
# Es el camino normal de la mazmorra
# 🚶 Aquí el jugador se mueve

# 🟠 2 → Grieta
# Es una zona peligrosa
# Puede representar una trampa
# Más adelante puede:
# Quitar vida ❤️
# Activar un evento ⚠️
# 💥 Piso dañado o peligroso

# 🦴 3 → Huesos
# Indican que alguien murió ahí
# Decoración o pista visual
# En el futuro puede:
# Esconder objetos 🎒
# Avisar de un enemigo 👀
# ☠️ Zona sospechosa

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