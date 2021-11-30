import pygame, random
from pygame.locals import *




def on_grid_random():
    x = random.randint(10,390)
    y = random.randint(10,390)
    return (x//10 * 10, y//10 * 10)


def random_color():
    r = random.randint(50,255)
    g = random.randint(50,255)
    b = random.randint(50,255)
    return r,g,b


def eat(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((400,400))
pygame.display.set_caption('Snake- Fillipe Vieira')

snake = [(200, 200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = on_grid_random()
apple = pygame.Surface((10,10))
apple.fill(random_color())

my_direction = LEFT 

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if my_direction != DOWN:
                    my_direction = UP
            if event.key == K_DOWN:
                if my_direction != UP:
                    my_direction = DOWN
            if event.key == K_LEFT:
                if my_direction != RIGHT:
                    my_direction = LEFT
            if event.key == K_RIGHT:
                if my_direction != LEFT:
                    my_direction = RIGHT

    if eat(snake[0], apple_pos):
        apple_pos = on_grid_random()
        apple.fill(random_color())
        snake.append((0,0))
        snake_skin.fill(random_color())
    
    

    for i in range(len(snake) -1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    
    if my_direction == LEFT and snake[0][0] == 0:
        my_direction = RIGHT
    if my_direction == RIGHT and snake[0][0] == 390:
        my_direction = LEFT
    if my_direction == UP and snake[0][1] == 0:
        my_direction = DOWN
    if my_direction == DOWN and snake[0][1] == 390:
        my_direction = UP

    screen.fill((20,20,20))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()