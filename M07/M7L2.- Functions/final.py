#pgzero
import random

WIDTH = 600 
HEIGHT = 300 

TITLE = "Persona Corredora" 
FPS = 30 



persona = Actor('stand', (50, 240))
background = Actor("background")
box = Actor('red', (550, 265))
new_image = 'stand' 
bee = Actor('bat', (550, 175))
go = Actor("GO")

game_over = 0
count = 0
enemy = random.randint(1,2)
speed = 5

def boxes():
    global count
    global enemy
    global speed
    if box.x > -20:
        box.x = box.x - speed
        box.angle = box.angle + 5
    else:
        box.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1
        
def bees():
    global count
    global enemy
    global speed
    global bee
    if bee.x > -20:
        bee.x = bee.x - speed
    else:
        bee.x = WIDTH + 20
        count = count + 1
        enemy = random.randint(1,2)
        speed = speed + 1
        bee.y = random.randint(120, 180)

def draw():
    background.draw()
    persona.draw()
    if enemy == 1:
        box.draw()
    else:
        bee.draw()
    screen.draw.text(count, pos=(10, 10), color="white", fontsize = 24)
    if game_over == 1:
        screen.draw.text('Press Enter', pos=(170, 150), color= "white", fontsize = 36)

    
def update(dt):
    global new_image
    global count
    global game_over
    global speed

    if enemy == 1:
        boxes()
    else:
        bees()

    if keyboard.left or keyboard.a and persona.x > 20:
        persona.x = persona.x - 5
        if new_image != 'left':
            persona.image = 'left'
            new_image = 'left'
    elif keyboard.right or keyboard.d and persona.x < 580:
        persona.x = persona.x + 5
        if new_image != 'right':
            persona.image = 'right'
            new_image = 'right'
    elif keyboard.down or keyboard.s:
        if new_image != 'duck':
            persona.image = 'duck'
            new_image = 'duck'
            persona.y = 250
    else:
        if persona.y > 240 and new_image == 'duck':
            persona.image = 'stand'
            new_image = 'stand'
            persona.y = 240
    
    if game_over == 1 and keyboard.enter:
        game_over = 0 
        count = 0
        persona.pos = (50, 240)
        box.pos = (550, 265)
        bee.pos = (550, 175)
        speed = 5

    if persona.colliderect(box) or persona.colliderect(bee):
        game_over = 1
       
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        persona.y = 100
        animate(persona, tween='bounce_end', duration=2, y=240)