from pygame import *

class Character(sprite.Sprite):
    def __init__(self, filename, size_x, size_y, x, y, speed):
        self.filename = filename
        self.size_x = size_x
        self.size_y = size_y
        self.img = transform.scale( image.load(self.filename), (self.size_x, self.size_y))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        window.blit(self.img, (self.rect.x, self.rect.y))

class Wall(Character):
   def __init__(self, size_x, size_y, x, y):
      self.size_x = size_x
      self.size_y = size_y
      self.img = Surface( (size_x, size_y) )
      self.rect = self.img.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.img.fill( (100, 100, 100) ) #RGB

window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))

display.set_caption("Catch")

bg = transform.scale(image.load("background.jpg"), (window_width, window_height))
# player1 = transform.scale( image.load("sprite1.png"), (50, 50))
player1 = Character("hero.png", 50, 50, 20, 10, 50)
# player2 = transform.scale( image.load("sprite2.Qpng"), (100, 100))
player2 = Character("cyborg.png", 50, 50, 300, 240, 1)
# add one more player
goal = Character("treasure.png", 50, 50, 600, 440, 3)

wall_list = []
wall_list.append( Wall(25, 200, 100, 0) )
wall_list.append( Wall(25, 200, 250, 125) )
wall_list.append( Wall(25, 200, 400, 0) )
wall_list.append( Wall(25, 200, 550, 125) )
wall_list.append( Wall(25, 200, 100, 200) )
wall_list.append( Wall(25, 200, 250, 325) )
wall_list.append( Wall(25, 200, 400, 200) )
wall_list.append( Wall(25, 200, 550, 325) )

game = True
finish = False

font.init()
print(font.get_fonts())
style = font.SysFont('arial', 50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(bg, (0, 0))
        player1.draw()
        player2.draw()
        goal.draw()
        for wall in wall_list:
            wall.draw()

        keys_pressed = key.get_pressed()

        if (keys_pressed[K_RIGHT] and player1.rect.x < window_width-player1.size_x):
            player1.rect.x += player1.speed
            for wall in wall_list:
                if(sprite.collide_rect(player1, wall)):
                    player1.rect.x -= player1.speed
        elif (keys_pressed[K_LEFT] and player1.rect.x > 0):
            player1.rect.x -= player1.speed
            for wall in wall_list:
                if(sprite.collide_rect(player1, wall)):
                    player1.rect.x += player1.speed
        elif (keys_pressed[K_UP] and player1.rect.y > 0):
            player1.rect.y -= player1.speed
            for wall in wall_list:
                if(sprite.collide_rect(player1, wall)):
                    player1.rect.y += player1.speed
        elif (keys_pressed[K_DOWN] and player1.rect.y < window_height-player1.size_x):
            player1.rect.y += player1.speed
            for wall in wall_list:
                if(sprite.collide_rect(player1, wall)):
                    player1.rect.y -= player1.speed
                    
        if (player2.rect.x > window_width):
            player2.speed *= -1 
        if (player2.rect.x  < 0):
            player2.speed *= -1
        player2.rect.x +=player2.speed

        if sprite.collide_rect(player1, player2):
            print("YOU LOSE")
            text = style.render("YOU LOSE",True, (214, 147, 118))
            window.blit(text, (350,250))
            finish = True
        if sprite.collide_rect(player1, goal):
            print("YOU WIN",True, (179, 245, 194))
            text = style.render("YOU WIN",True, (179, 245, 194))
            window.blit(text, (350,250))
            finish = True
    display.update()