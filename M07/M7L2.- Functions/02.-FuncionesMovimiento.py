#pgzero
#TRASLADAR LA LOGICA DE UPDATE Y COLOCARLO EN boxes() y bees() y llamar la fn en update()
WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana


TITLE = "Corredor de Alienígenas" # Título para la ventana de juego
FPS = 30 #  Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240)) 
background = Actor("background") 
box = Actor('box', (550, 265)) 
new_image = 'alien' #Seguimiento de la imagen actual 
bee = Actor('bee', (850, 175)) 
go = Actor("GO") 
game_over = 0
count = 0

def boxes():#🔴🔴🔴🔴
    global count#🔴🔴🔴🔴
    #  Movimiento de la caja#🔴🔴🔴🔴
    if box.x > -20:#🔴🔴🔴🔴
        box.x = box.x - 5#🔴🔴🔴🔴
        box.angle = box.angle + 5#🔴🔴🔴🔴
    else:#🔴🔴🔴🔴
        box.x = WIDTH + 20#🔴🔴🔴🔴
        count = count + 1#🔴🔴🔴🔴

def bees(): #🔴🔴🔴🔴
    global count#🔴🔴🔴🔴
    # Movimiento de la abeja#🔴🔴🔴🔴
    if bee.x > -20:#🔴🔴🔴🔴
        bee.x = bee.x - 5#🔴🔴🔴🔴
    else:#🔴🔴🔴🔴
        bee.x = WIDTH + 20#🔴🔴🔴🔴
        count = count + 1#🔴🔴🔴🔴

def draw():
    background.draw()
    alien.draw()
    box.draw()
    bee.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24) 
    if game_over == 1:
        go.draw()
        screen.draw.text('Press Enter', pos=(170, 150), color= "white", fontsize = 36) 

    
def update(dt):
    # Variables
    global new_image
    global count
    global game_over
    
    # Llamando funciones
    boxes() #🔴🔴🔴🔴
    bees() #🔴🔴🔴🔴
    
    # Controles
    if keyboard.left or keyboard.a and alien.x > 20: 
        alien.x = alien.x - 5
        if new_image != 'left':
            alien.image = 'left'
            new_image = 'left'
    elif keyboard.right or keyboard.d and alien.x < 580: 
        alien.x = alien.x + 5
        if new_image != 'right':
            alien.image = 'right'
            new_image = 'right'
    elif keyboard.down or keyboard.s: 
        if new_image != 'duck':
            alien.image = 'duck'
            new_image = 'duck'
            alien.y = 250
    else:
        if alien.y > 240 and new_image == 'duck':
            alien.image = 'alien'
            new_image = 'alien'
            alien.y = 240
    
    if game_over == 1 and keyboard.enter: 
        game_over = 0 
        count = 0
        alien.pos = (50, 240)
        box.pos = (550, 265)
        bee.pos = (850, 175)
    
    # Colisión
    if alien.colliderect(box) or alien.colliderect(bee): 
        game_over = 1

# Salto        
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w: 
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240) 