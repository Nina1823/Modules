#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Alien Runner" # Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objects
alien = Actor('alien', (50, 240)) # Se crea un actor llamado 'alien'/marcianito ubicado en la posición (50, 240)
background = Actor("background") # Se crea un actor llamado 'background' que representa el fondo del juego
box = Actor('box', (550, 265)) # Se crea un actor llamado 'box'/caja ubicado en la posición (550, 265)
new_image = 'alien' #Variable que guarda la imagen actual del alien (permite cambiarla según el movimiento)


def draw(): #FUNCIÓN QUE DIBUJA LOS OBJETOS EN LA PANTALLA
    background.draw() # Dibuja el fondo
    alien.draw() # Dibuja el alien
    box.draw() # Dibuja la caja
    
def update(dt): #FUNCIÓN QUE ACTUALIZA LA POSICIÓN DE LOS OBJETOS
    global new_image # Se indica que se usará la variable global new_image para poder cambiar la imagen del alien 
    # Movimiento de la caja
    if box.x > -20: # Si la caja no ha salido de la pantalla
        box.x = box.x - 5 # Mueve la caja 5 píxeles a la izquierda
        box.angle = box.angle + 5 # Rota la caja 5 grados
    else: # Si la caja ha salido de la pantalla
        box.x = WIDTH + 20 # La reposiciona a la derecha de la pantalla
        
    # Controles
    if keyboard.left or keyboard.a and alien.x > 20: # Si se presiona la flecha izquierda o la tecla 'a' y el alien no ha llegado al borde izquierdo de la pantalla 
        alien.x = alien.x - 5 # Mueve el alien 5 píxeles a la izquierda
        if new_image != 'left': # Si la imagen actual no es 'left' (izquierda)
            alien.image = 'left' # Cambia la imagen del alien a 'left'
            new_image = 'left' # Actualiza la variable new_image a 'left'
    elif keyboard.right or keyboard.d and alien.x < 580: # Si se presiona la flecha derecha o la tecla 'd' y el alien no ha llegado al borde derecho de la pantalla 
        alien.x = alien.x + 5 # Mueve el alien 5 píxeles a la derecha
        if new_image != 'right': # Si la imagen actual no es 'right' (derecha)
            alien.image = 'right' # Cambia la imagen del alien a 'right'
            new_image = 'right' # Actualiza la variable new_image a 'right'
    else: # Si no se presiona ninguna tecla de movimiento
        alien.image = 'alien' # Cambia la imagen del alien a 'alien' (posición neutral)
        new_image = 'alien' # Actualiza la variable new_image a 'alien'

def on_key_down(key): #FUNCIÓN QUE SE EJECUTA CUANDO SE PRESIONA UNA TECLA
    # Salto
    if keyboard.space or keyboard.up or keyboard.w: # Si se presiona la barra espaciadora, la flecha arriba o la tecla 'w' 
        alien.y = 100 # Cambia la posición vertical del alien para simular un salto
        animate(alien, tween='bounce_end', duration=2, y=240) # Anima el alien para que vuelva a la posición original con un efecto de rebote
