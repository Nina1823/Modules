#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Clicker animal"
FPS = 30

# Objetos
animal = Actor("giraffe", (150, 250))
background = Actor("background")
bonus_1 = Actor("bonus", (450, 100)) #🔴
bonus_2 = Actor("bonus", (450, 200)) #🔴

# Variables
count = 0
click = 1

def draw():
    background.draw()
    animal.draw()
    screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)
    bonus_1.draw() #🔴
    screen.draw.text("+1$ cada 2s", center=(450, 80), color="black", fontsize = 20) #🔴
    screen.draw.text("PRECIO: 15$", center=(450, 110), color="black", fontsize = 20) #🔴
    bonus_2.draw() #🔴
    screen.draw.text("+15$ cada 2s", center=(450, 180), color="black", fontsize = 20) #🔴
    screen.draw.text("PRECIO: 200$", center=(450, 210), color="black", fontsize = 20) #🔴

def on_mouse_down(button, pos):
    global count
    global click
    if button == mouse.LEFT:
        #  Click en el objeto animal
        if animal.collidepoint(pos):
            count += click
            animal.y = 200
            animate(animal, tween='bounce_end', duration=0.5, y=250)