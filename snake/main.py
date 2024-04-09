import pygame 
import random 
pygame.init()


# pygame setup
screen_width = 800 
screen_height = 800 
pixel_size = 40 

pixel_grid_max_x = int(screen_width / pixel_size)
pixel_grid_max_y = int(screen_height / pixel_size)

# colours 
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
colours = [red,green,blue]
# snake 
"""
inserts realtime snake coordinates to the front of the queue  
always remove the last item in the queue 
this way your snake head will always be updated and the body holds the value of the previous head
current information first then the history continues on [new,old,older,oldest] when oldest is removed 
its called first in first out because if you had a line of people the first person (oldest value) gets removed first before the newer person (new value) gets moved to the position of whos infront of them 
"""
position = "STATIC"
snake_x = screen_width / 2 
snake_y =  0 
snake_width = pixel_size
snake = [] 
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
        snake.append(current)



    screen.fill("black")
    # draw snake on screen 
    # left, top, width, height

    current = (snake_x,snake_y,snake_width,pixel_size)
    snake.insert(0,current)



        
    print(snake)
    for part in enumerate(snake):
        if part[0] == 0: # head
            pygame.draw.rect(screen, blue,part[1])
        else:

            pygame.draw.rect(screen, red,part[1])


    snake.remove(snake[-1])

    # draw apple on screen 
    pygame.draw.rect(screen, green,(apple_x,apple_y,pixel_size,pixel_size))


    # RENDER YOUR GAME HERE
    pygame.display.flip()
    clock.tick(15)  # FPS

pygame.quit()