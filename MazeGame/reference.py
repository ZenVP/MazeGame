from pygame import *

class Character():
    def __init__(self, filename, size_x, size_y, x, y, speed):
        self.filename = filename
        self.size_x = size_x
        self.size_y = size_y
        self.x = x
        self.y = y
        self.img = transform.scale( image.load(self.filename), (self.size_x, self.size_y))
        self.speed = speed
    def draw(self):
        window.blit(self.img, (self.x, self.y))

window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))

display.set_caption("Catch")

bg = transform.scale(image.load("background.jpg"), (window_width, window_height))
# player1 = transform.scale( image.load("sprite1.png"), (50, 50))
player1 = Character("hero.png", 50, 50, 300, 100, 3)
# player2 = transform.scale( image.load("sprite2.png"), (100, 100))
player2 = Character("cyborg.png", 50, 50, 300, 300, 3)
# add one more player
goal = Character("treasure.png", 50, 50, 400, 400, 3)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(bg, (0, 0))
    player1.draw()
    player2.draw()
    goal.draw

    keys_pressed = key.get_pressed()

    if (keys_pressed[K_RIGHT] and player1.x < window_width-player1.size_x):
        player1.x += player1.speed
    elif (keys_pressed[K_LEFT] and player1.x > 0):
        player1.x -= player1.speed
    elif (keys_pressed[K_UP] and player1.y > 0):
        player1.y -= player1.speed
    elif (keys_pressed[K_DOWN] and player1.y < window_height-player1.size_x):
        player1.y += player1.speed

    if (keys_pressed[K_d] and player2.x < window_width-player2.size_y):
        player2.x += player2.speed
    elif (keys_pressed[K_a] and player2.x > 0):
        player2.x -= player2.speed
    elif (keys_pressed[K_w] and player2.y > 0):
        player2.y -= player2.speed
    elif (keys_pressed[K_s] and player2.y < window_height-player2.size_y):
        player2.y += player2.speed

    display.update()