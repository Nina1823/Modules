#pgzero

WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana


TITLE = "Araña" # Título para la ventana de juego
FPS = 30 #  Número de fotogramas por segundo

# Objects
spider = Actor('spider', (150, 150))
block1 = Actor('block', (100, 250))
block2 = Actor('block', (30, 30))
block3 = Actor('block', (270, 120))
background = Actor("bg")
coll = 0 #🔴

def draw():
    background.draw()
    spider.draw()
    block1.draw()
    block2.draw()
    block3.draw()
    if coll == 1:
        screen.draw.text('Has chocado con un bloque', pos=(10, 150), color= "white", fontsize = 24)#🔴
    elif coll == 2:#🔴
        screen.draw.text('Has chocado con una pared', pos=(10, 150), color= "white", fontsize = 24)#🔴
        
def update(dt):
    # Controles
    global coll  # 🔴
    if keyboard.left and spider.x > 20:
        spider.x -= 5
    elif keyboard.right and spider.x < 280:
        spider.x += 5
    elif keyboard.up and spider.y > 20:
        spider.y -= 5
    elif keyboard.down and spider.y < 280:
        spider.y += 5
    
    # Colisiones
    if spider.colliderect(block1) or spider.colliderect(block2) or spider.colliderect(block3):  # 🔴
        coll = 1 # 🔴
    elif spider.x >= 280 or spider.x <= 20 or spider.y <= 20 or spider.y >= 280: # 🔴
        coll = 2 # 🔴
    else: # 🔴
        coll = 0 # 🔴