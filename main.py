import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))

runnin = True

class Padel:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def draw(self):
        pygame.draw.rect(window, "white", (self.x, self.y, self.w, self.h))

p1 = Padel(10, 10, 30, 150)
p2 = Padel(360, 10, 30, 150)

while runnin:
    p1.draw()
    p2.draw()
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            runnin = False

    pygame.display.update()

pygame.quit()