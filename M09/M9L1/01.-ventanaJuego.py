# Hoy vamos a empezar a desarrollar un juego del género Roguelike. 
# Nuestro juego tendrá una característica especial: todo el campo de juego estará formado por
# celdas. Todos los enemigos se generarán aleatoriamente, se mostrará una bonificación cuando 
# un enemigo pierda, y el resultado del juego será siempre impredecible.
# La característica del género es que el nivel se genera aleatoriamente. En nuestro juego, 
# nosotros mismos diseñaremos el mapa, pero todo lo demás se generará usando el módulo random.


# EN QUE CONSISITE
# Mazmorras es un juego Roguelike donde el jugador controla un personaje que explora una mazmorra formada por celdas. 
# El personaje se mueve por el mapa, tiene vida y ataque, y el objetivo es recorrer la mazmorra mientras se prepara para futuros desafíos como
# enemigos y trampas.

# #pgzero

# Ventana de juego hecha de celdas
cell = Actor('border') # 🟡🔵{🟢} 👁️ quite el cell = 50 y poner es el Actor
size_w = 5 # Anchura del campo en celdas
size_h = 5 # Altura del campo en celdas
WIDTH = cell.width * size_w # 🟡🔵🟢 se agrega a la cell el ..width
HEIGHT = cell.height * size_h # 🟡🔵🟢 se agrega a la cell el ..height

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo