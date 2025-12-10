#pgzero

WIDTH = 600
HEIGHT = 400

TITLE = "Clicker animal"
FPS = 30

# Objetos
animal = Actor("giraffe", (150, 250))
background = Actor("background")

# Variables
count = 0
click = 1 #🔴

def draw():
    background.draw()
    animal.draw()
    screen.draw.text(count, center=(150, 100), color="white", fontsize = 96)


def on_mouse_down(button, pos): #🔴
    global count #🔴
    if button == mouse.LEFT: #🔴
        # Click en el botón animal
        if animal.collidepoint(pos): #🔴
            count += click #🔴
            animal.y = 200 #🔴
            animate(animal, tween='bounce_end', duration=0.5, y=250) #🔴