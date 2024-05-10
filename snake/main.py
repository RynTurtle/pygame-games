import pygame 
import random 
screen_width = 840 
screen_height = 840 

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)
pixel_size = 40 


class Snake():
    def __init__(self):
        self.direction = "STATIC" 
        self.snake_y = 0 
        self.snake_x = 0 
        self.snake_body = []

    # sets the direction the snake should move in  
    def set_head_direction(self,direction):
        self.direction = direction 
 
    # changes the snake position based on the direction 
    def move(self):
        # change the x and y coordinates based on movements given 
        if self.direction == "UP":
            self.snake_y -= pixel_size 
        if self.direction == "DOWN":
            self.snake_y += pixel_size 
        if self.direction == "LEFT":
            self.snake_x -= pixel_size 
        if self.direction  == "RIGHT":
            self.snake_x += pixel_size 

    def grow(self):
        self.snake_body.insert(0,self.head_position)

    def draw(self):
        self.head_position = (self.snake_x,self.snake_y,pixel_size,pixel_size)
        self.snake_body.insert(0,self.head_position) # insert the new head position 
        for body in self.snake_body: # draw the entire snake 
            pygame.draw.rect(screen,green,body)
        # remove the tail so all the values are updated 
        self.snake_body.remove(self.snake_body[-1]) 

    def body(self):
        return self.snake_body 


class Apple():
    def __init__(self):
        pass 

    def spawn():
        pass 
    
    def position():
        pass 
    
class Snake_Game():
    def __init__(self):
        self.pixel_grid_max_x = int(screen_width / pixel_size)
        self.pixel_grid_max_y = int(screen_height / pixel_size)
        self.clock = pygame.time.Clock()
        self.running = True 

        self.snake = Snake()

    def keypress_events(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.snake.set_head_direction("UP")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.snake.set_head_direction("DOWN")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.snake.set_head_direction("LEFT")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.snake.set_head_direction("RIGHT")


    def collision():
        # if snake touches snake 
        # if snake touches border of game
        # if snake touches apple 
        pass 


    def checkered_background(self):
        i  = 0 
        for y in range(self.pixel_grid_max_y):
            for x in range(self.pixel_grid_max_x):
                if (i % 2  == 0): # even black odd white
                    colour = black
                else:
                    colour = white 
                rectangle_position = (y * pixel_size,x * pixel_size,pixel_size,pixel_size)
                pygame.draw.rect(screen, colour,rectangle_position)
                i += 1


    def start(self):
        while self.running:
            for event in pygame.event.get():
                self.keypress_events(event)
            self.checkered_background()


            self.snake.draw()
            self.snake.move()

            pygame.display.flip()
            self.clock.tick(15)  # FPS

Snake_Game().start()