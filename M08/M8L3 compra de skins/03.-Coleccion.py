#dispondremos de una colección, un almacén donde se guardarán todas las pieles que hayamos comprado.
#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Clicker animal"
FPS = 30

# Objetos
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
play = Actor("play", (300, 100))
cross = Actor("cross", (580, 20))
shop = Actor("tienda", (300, 200))
collection = Actor("coleccion", (300, 300)) 
crocodile = Actor('crocodile', (120, 200)) 
hippo = Actor('hippo', (300, 200)) 

# Variables
count = 0
click = 1
mode = 'menu'
price_1 = 15
price_2 = 200
price_3 = 600
animals = [] # 🔴

def draw():
    if mode == 'menu':
        background.draw()
        play.draw()
        screen.draw.text(count, center=(50, 20), color="white", fontsize = 36)
        shop.draw()
        collection.draw()
   
    elif mode == 'game':    
        background.draw()
        animal.draw()
        screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(price_1, center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(price_2, center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("+50$ cada 2s", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(price_3, center=(450, 310), color="black", fontsize = 20)
        cross.draw()
    
    elif mode == 'shop': 
        background.draw()
        if crocodile not in animals: # 🔴 
          crocodile.draw() 
          screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36) 
        if hippo not in animals: # 🔴
          hippo.draw() 
          screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36) 
        if len(animals) > 2: # 🔴
          screen.draw.text("Ya has comprado todas las opciones", center= (300, 200), color="white", fontsize = 36) 
        cross.draw() 
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36) 

    elif mode == 'collection': # 🔴
        background.draw() # 🔴
        for i in range(len(animals)): # 🔴
            animals[i].draw() # 🔴
        cross.draw() # 🔴
        screen.draw.text(count, center=(30, 20), color="white", fontsize = 36) # 🔴
        if len(animals) == 0:
          screen.draw.text("No has adquirido ninguna piel aun", center= (300, 200), color="white", fontsize = 36) 
        if crocodile in animals: # 🔴
          screen.draw.text("+2$", center= (120, 300), color="white", fontsize = 36) # 🔴
        if hippo in animals: # 🔴
          screen.draw.text("+3$", center= (300, 300), color="white", fontsize = 36) # 🔴


def for_bonus_1():
    global count
    count += 1

def for_bonus_2():
    global count
    count += 15

def for_bonus_3():
    global count
    count += 50

def on_mouse_down(button, pos):
    global count
    global click
    global mode
    global price_1, price_2, price_3
    if button == mouse.LEFT and mode == 'game':
        # Click en el objeto animal
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)
        # Click en el botón bonus_1  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if count >= price_1:
                schedule_interval(for_bonus_1, 2)
                count -= price_1
                price_1 *= 2
        # Click en el botón bonus_2
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if count >= price_2:
                schedule_interval(for_bonus_2, 2)
                count -= price_2
                price_2 *= 2
        #Click en el botón bonus_3
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if count >= price_3:
                schedule_interval(for_bonus_3, 2)
                count -= price_3
                price_3 *= 2
    if cross.collidepoint(pos): 
        mode = 'menu' 

    
    # Modo menú
    elif mode == 'menu' and button == mouse.LEFT:
        if play.collidepoint(pos):
            mode = 'game'
        elif shop.collidepoint(pos): 
            mode = 'shop' 
        elif collection.collidepoint(pos): # 🔴 
            mode = 'collection' # 🔴

    elif mode == 'shop' and button == mouse.LEFT: 
        if cross.collidepoint(pos): 
            mode = 'menu' 
  
        elif crocodile.collidepoint(pos):
        #    crocodile.y = 180 # 🔴 🟢 🔰
        #    animate(crocodile, tween='bounce_end', duration=0.5, y=200) # 🔴 🟢 🔰
            if crocodile in animals: # 🔴
                animal.image = 'crocodile' # 🔴
            elif count >= 500: 
                count -= 500 
                click = 2 
                animal.image = 'crocodile'
                animals.append(crocodile) # 🔴 
  
        elif hippo.collidepoint(pos):
            if hippo in animals: # 🔴
                animal.image = 'hippo' # 🔴 
            if count >= 2500: 
                count -= 2500 
                click = 3 
                animal.image = 'hippo' 
                animals.append(hippo) # 

    elif  mode == 'collection' and button == mouse.LEFT: # 🔴
        if cross.collidepoint(pos): # 🔴
            mode = 'menu' # 🔴
        # Eligiendo un cocodrilo
        elif crocodile.collidepoint(pos): # 🔴
        #    crocodile.y = 180 # 🔴 🟢 🔰
        #    animate(crocodile, tween='bounce_end', duration=0.5, y=200) # 🔴 🟢 🔰
            if crocodile in animals: # 🔴
                animal.image = 'crocodile' # 🔴
        # Eligiendo un hipopótamo    
        elif hippo.collidepoint(pos): # 🔴
            if hippo in animals: # 🔴
                animal.image = 'hippo' # 🔴