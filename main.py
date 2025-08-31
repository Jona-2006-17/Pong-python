import pygame
import random
pygame.init()

window = pygame.display.set_mode((400, 400))

runnin = True
clock = pygame.time.Clock()
FPS = 60

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 5
        self.dx = random.uniform(-1,1)
        self.dy = random.uniform(-1,1)
        self.color = "blue"
        self.speed = 5
    
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), 7, self.w)

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        

        
class Padel:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 40
    
    def draw(self):
        pygame.draw.rect(window, "white", (self.x, self.y, self.w, self.h))

p1 = Padel(10, 10, 30, 150)
p2 = Padel(360, 10, 30, 150)
ball = Ball(100, 100)

def movimientos(padel1: Padel, padel2: Padel):
    window.fill("black")
    if keys[pygame.K_w]:
        padel1.y -= 0.1 * padel1.speed
    
    if keys[pygame.K_s]:
        padel1.y += 0.1 * padel1.speed

    if keys[pygame.K_UP]:
        padel2.y -= 0.1 * padel2.speed
    
    if keys[pygame.K_DOWN]:
        padel2.y += 0.1 * padel2.speed

while runnin:
    clock.tick(FPS)
    p1.draw()
    p2.draw()
    ball.draw()
    ball.move()
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            runnin = False

    keys = pygame.key.get_pressed()
    pygame.display.update()

    movimientos(p1, p2)


pygame.quit()