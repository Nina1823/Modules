#pgzero

WIDTH = 600 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Alien Runner" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Objetos
alien = Actor('alien', (50, 240))
background = Actor("background")
box = Actor('box', (850, 265))
bee = Actor('bee', (550, 160))
go = Actor('GO')
new_image = "alien"
game_over = 0
count_bee = 0
count_box = 0 

    #Pintar
def draw():
    global game_over
    if game_over == 0:
        background.draw()
        alien.draw()
        box.draw()
        bee.draw()
        screen.draw.text("🐝 Esquivadas" + str(count_bee), pos=(10,10), color="black", background="white", fontsize=24)
        screen.draw.text("📦 Esquivadas" + str(count_box), pos=(10,50), color="black", background="white", fontsize=24)
    if game_over == 1: 
        go.draw()
        screen.draw.text("Presiona Enter para continuar", center=(300,210), color="red", fontsize=38)
        
    
    #movimeintos
def update(dt):
    global new_image, game_over, count_bee, count_box
    if game_over == 0:
        # Movimiento de la caja
        if box.x > -20:
            box.x = box.x - 5
            box.angle = box.angle + 5
        else:
            box.x = WIDTH + 20
            count_box += 1
         # Movimiento de la abeja
        if bee.x > -20:
            bee.x = box.x - 5
        else:
            bee.x = WIDTH + 20
            count_bee += 1
        # Controles
        if keyboard.left or keyboard.a and alien.x > 20:
            alien.x = alien.x - 5
            if new_image != "left": 
                alien.image = "left"
                new_image = "left"
        elif keyboard.right or keyboard.d and alien.x < 580:
            alien.x = alien.x + 5 
            if new_image != "right":
                alien.image = "right"
                new_image = "right"
        elif keyboard.down or keyboard.s:
            if new_image != "duck": 
                alien.image = "duck"
                new_image = "duck"
                alien.y = 250
        else: 
            if alien.y > 240 and new_image == "duck":
                alien.image = "alien"
                new_image = "alien"
                alien.y = 240
                
    if game_over == 1 and keyboard.enter: 
        game_over = 0
        new_image = "alien"
        alien.image = "alien"
        bee.pos = (850, 130)
        box.pos = (550, 265)
        alien.pos = (50, 240)
        count_bee = 0
        count_box = 0 
        
    # COLISIÓN DE OBJETOS <CAJA Y ALIEN>
    if alien.colliderect(box) or alien.colliderect(bee): 
        game_over = 1    
            
# Salto
def on_key_down(key):
    global new_image
    if keyboard.space or keyboard.up or keyboard.w:
        if new_image != "alien": 
            alien.image = "alien"
            new_image = "alien"
        alien.y = 180
        animate(alien, tween="bounce_end", duration=2, y=240)