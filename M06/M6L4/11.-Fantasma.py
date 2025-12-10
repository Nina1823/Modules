#pgzero

WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 #Altura de la ventana

TITLE = "Ghost in a Castle" # Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
ghost = Actor('ghost', (150, 150))
background = Actor("bg")

def draw():
    background.draw()
    ghost.draw()

def update(dt): #🔴
    if keyboard.left and ghost.x > 20: #🔴
        ghost.x -= 5 #🔴
        
    elif keyboard.right and ghost.x < 280: #🔴
        ghost.x += 5 #🔴
    
    elif keyboard.up and ghost.y > 20: #🔴
        ghost.y -= 5 #🔴
        
    elif keyboard.down and ghost.y < 280: #🔴
        ghost.y += 5 #🔴
        
def on_key_down(key): #🔴
    if keyboard.space and ghost.image == 'ghost1': #🔴
        ghost.image = 'ghost' #🔴
    elif keyboard.space and ghost.image == 'ghost': #🔴
        ghost.image = 'ghost1' #🔴