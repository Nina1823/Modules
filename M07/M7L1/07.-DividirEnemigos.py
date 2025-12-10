#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Corredor de Alienígenas" # Título para la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (550, 265))
new_image = 'alien' #Seguimiento de la imagen actual
bee = Actor('bee', (850, 175)) #Abeja
go = Actor("GO")
game_over = 0
count = 0

def draw():
    background.draw()
    alien.draw()
    box.draw()
    bee.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    if game_over == 1:
        go.draw()
        screen.draw.text('Presiona Enter', pos=(170, 170), color= "white", fontsize = 36)
        screen.draw.text('Te has estrellado contra una caja', pos=(60, 200), color= "white", fontsize = 36)
    elif game_over == 2:
        go.draw()
        screen.draw.text('Presiona Enter', pos=(170, 170), color= "white", fontsize = 36)
        screen.draw.text('Te has estrellado contra una abeja', pos=(60, 200), color= "white", fontsize = 36)

def update(dt):
    global new_image
    global game_over
    global count
    # Movimiento de la abeja
    if game_over == 0:
        if bee.x > -20:
            bee.x = bee.x - 5
        else:
            bee.x = WIDTH + 20
            count = count + 1
            
        # Movimiento de la caja
        if box.x > -20:
            box.x = box.x - 5
            box.angle = box.angle + 5
        else:
            box.x = WIDTH + 20
            count = count + 1
            
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
            new_image = 'alien' 
            alien.image = 'alien' 
            alien.pos = (50, 240) 
            box.pos = (550, 265) 
            bee.pos = (850, 175) 
        
        # Colisión
        if alien.colliderect(box): #🔴
            game_over = 1 #🔴
        elif alien.colliderect(bee): #🔴
            game_over = 2 #🔴
        
def on_key_down(key):
    global new_image 
    if keyboard.space or keyboard.up or keyboard.w:
        if new_image != 'alien': 
            alien.image = 'alien' 
            new_image = 'alien'  
        alien.y = 100
        animate(alien, tween='bounce_end', duration=2, y=240)