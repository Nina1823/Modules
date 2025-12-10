#pgzero

WIDTH = 300 # Ancho de la ventana
HEIGHT = 300 # Altura de la ventana

TITLE = "Clicker" # Título de la ventana de juego
FPS = 30 # Fotogramas por segundo
count = 0

def draw():
    screen.fill((32, 191, 107))
    screen.draw.text(count, center=(150, 150), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global count
    if button == mouse.LEFT:
        count = count + 1
        