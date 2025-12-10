#pgzero

WIDTH = 600
HEIGHT = 450

TITLE = "Viaje al espacio 🚀"
FPS = 30

# Objetos y variables
ship = Actor("ship", (300, 400))
space = Actor("space")

# Elaboración
def draw():
    space.draw()
    ship.draw()
    
# Controles #🔴🟢🔵🟡
def on_mouse_move(pos): #🔴🟢🔵🟡
    ship.pos = pos #🔴🟢🔵🟡