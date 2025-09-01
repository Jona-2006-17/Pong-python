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
        self.radius = 6
        self.dx = random.uniform(-1,1)
        self.dy = random.uniform(-1,1)
        self.color = "blue"
        self.speed = 5
    
    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius, self.w)

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

        if self.y <=0 or self.y >= 400:
            self.dy *= -1

    def get_react(self):
        return pygame.Rect(self.x - self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        
    def bounce_padel(self):
        self.dx *= -1
    
        
class Padel:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = 40
    
    def draw(self):
        pygame.draw.rect(window, "white", (self.x, self.y, self.w, self.h))

    def get_react(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
    
    def check_collisions(self, ball):
        return self.get_react().colliderect(ball.get_react())

    def update(self, ball):
        self.draw()
        if self.check_collisions(ball):
            ball.bounce_padel()

p1 = Padel(20, 10, 10, 140)
p2 = Padel(370, 10, 10, 140)
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
    p1.update(ball)
    p2.update(ball)
    ball.draw()
    ball.move()
    for envent in pygame.event.get():
        if envent.type == pygame.QUIT:
            runnin = False

    keys = pygame.key.get_pressed()
    pygame.display.update()

    movimientos(p1, p2)


pygame.quit()