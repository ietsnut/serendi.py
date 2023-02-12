import sys, pygame
import Q

gates = ['x', 'x', 'x', 'x', 'h', 'h', 'x', 'h', 'x', 'h', 't', 'x', 'x']
q = Q.state(1)
step = 0

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WHITE = (255, 255, 255)
ZERO = (0 ,0)
CROPRECT = (250, 0, 500, 1000)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

x = pygame.image.load("x.jpg")
t = pygame.image.load("t.jpg")
h = pygame.image.load("h.jpg")

print(q.state)

def eval():
    if step < len(gates) and step >= 0:
        getattr(q, gates[step])(0)
    print(q.state)
            
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                eval()
                step -= 1
            if event.key == pygame.K_UP:
                eval()
                step += 1
    screen.fill(WHITE)
    if step < len(gates) and step >= 0:
        img = globals()[gates[step]]
        screen.blit(img, ZERO)
        if q.state[0] == 0 or q.state[1] < 0:
            img_copy = img.copy()
            img = pygame.transform.flip(img_copy, False, True)
            screen.blit(img, ZERO)
        if q.state[0] != 0 and q.state[1] != 0:
            screen.blit(img, ZERO, CROPRECT)
            screen.blit(img, (500, 0), CROPRECT)

    pygame.display.update()

pygame.quit()