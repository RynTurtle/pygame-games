import pygame
import random
# pygame setup
pygame.init()

screen_width = 800
screen_height = 800
pixel_size = 40 

pixel_grid_max_x = int(screen_width / pixel_size)
pixel_grid_max_y = int(screen_height / pixel_size)

# colours 
red = (255,0,0,)
green = (0, 255, 0)


# snake 
position = "STATIC"
snake_x = screen_width / 2 
snake_y =  0 
snake_width = pixel_size 


# apple
spawn_apple = True
apple_x = 0 
apple_y = 0 

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                position = "UP"
            if event.key == pygame.K_DOWN:
                position = "DOWN"
            if event.key == pygame.K_LEFT:
                position = "LEFT"
            if event.key == pygame.K_RIGHT:
                position = "RIGHT"
    screen.fill("black")
    if position == "UP":
        snake_y -= pixel_size
    if position == "DOWN":
        snake_y += pixel_size
    if position == "LEFT":
        snake_x -= pixel_size
    if position == "RIGHT":
        snake_x += pixel_size
        
    if snake_x > screen_width or snake_x < 0:
        running = False 
    if snake_y > screen_height or snake_y < 0:
        running = False 

    if spawn_apple == True:
        apple_x = random.randrange(0,pixel_grid_max_x) * pixel_size
        apple_y = random.randrange(0,pixel_grid_max_y) * pixel_size
        spawn_apple = False 

    
    if snake_x == apple_x and snake_y == apple_y:
        spawn_apple = True
        print("nom")

    # draw snake on screen 
    # left, top, width, height
    snake = (snake_x,snake_y,snake_width,pixel_size)
    pygame.draw.rect(screen, red,snake)

    # draw apple on screen 
    pygame.draw.rect(screen, green,(apple_x,apple_y,pixel_size,pixel_size))


    # RENDER YOUR GAME HERE
    pygame.display.flip()
    clock.tick(15)  # FPS

pygame.quit()

