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

def movimientos(padel1: Padel, padel2: Padel):
    window.fill("black")
    if keys[pygame.K_w]:
        padel1.y -= 0.1
    
    if keys[pygame.K_s]:
        padel1.y += 0.1

    if keys[pygame.K_UP]:
        padel2.y -= 0.1
    
    if keys[pygame.K_DOWN]:
        padel2.y += 0.1

while runnin:
    p1.draw()
    p2.draw()
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            runnin = False

    keys = pygame.key.get_pressed()
    pygame.display.update()

    movimientos(p1, p2)


pygame.quit()