#pgzero

#CONFIGURACIÓN GENERAL VENTANA
WIDTH = 600
HEIGHT = 400
TITLE = "Clicker animal"
FPS = 30

# OBJETOS DEL JUEGO
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
play = Actor("play", (300, 100))
cross = Actor("cross", (580, 20))
shop = Actor("tienda", (300, 200)) 
collection = Actor("coleccion", (300, 300)) 

# VARIABLES DEL JUEGO
count = 0
click = 1
mode = 'menu'
price_1 = 15 
price_2 = 200 
price_3 = 600 

# F() DRAW PARA DIBUJAR LOS OBJETOS
def draw():
    # Dibuja el fondo y los objetos para el modo menu o pantalla inicial
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(50, 20), color="white", fontsize = 36)
        shop.draw() 
        collection.draw() 
   # dibuja el fondo y los objetos para el modo juego activo
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("PRECIO: "+str(price_1), center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("PRECIO: "+str(price_2), center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw() 
        screen.draw.text("+50$ cada 2s", center=(450, 280), color="black", fontsize = 20) 
        screen.draw.text("PRECIO: "+str(price_3), center=(450, 310), color="black", fontsize = 20) 
        cross.draw()

# F1() PARA BONOS PARA ACTUALIZAR EL JUEGO
def for_bonus_1():
    global count
    count += 1

# F2() PARA BONOS PARA ACTUALIZAR EL JUEGO
def for_bonus_2():
    global count
    count += 15

# F3() PARA BONOS PARA ACTUALIZAR EL JUEGO
def for_bonus_3():
    global count
    count += 50

#FUNCIONES PARA MANEJAR LOS EVENTOS DEL RATÓN & PROCESAMIENTO DE CLICKS
def on_mouse_down(button, pos):
    global count
    global mode
    global price_1
    global price_2 
    global price_3
    if button == mouse.LEFT and mode == 'game':
        # Click en el objeto animal
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Click en el botón bonus_1  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            bonus_1.x = 455
            animate(bonus_1, tween='bounce_end', duration=0.2, x= 450, y=100)
            if count >= price_1:
                schedule_interval(for_bonus_1, 2)
                count -= price_1
                price_1 *= 2 
        # Click en el botón bonus_2
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            bonus_2.x = 455
            animate(bonus_2, tween='bounce_end', duration=0.2, x= 450, y=200)
            if count >= price_2:
                schedule_interval(for_bonus_2, 2)
                count -= price_2
                price_2 *= 2 
        # Click en el botón bonus_3
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            bonus_3.x = 455
            animate(bonus_3, tween='bounce_end', duration=0.2, x= 450, y=300)
            if count >= price_3:
                schedule_interval(for_bonus_3, 2)
                count -= price_3
                price_3 *= 2 
        # DETECCIÓN DE CLIC EN BOTON MENÚ
        elif cross.collidepoint(pos):
            mode = 'menu'
    
    # Detección de clic en el botón de inicio del juego
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'