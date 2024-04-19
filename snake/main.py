import pygame 
import random 
class Apple():
    def __init__(self,screen,apple_colour,grid_max_x,grid_max_y,apple_pixel_size):
        self.apple_colour = apple_colour
        self.apple_x = 0
        self.apple_y = 0
        self.grid_max_x = grid_max_x
        self.grid_max_y = grid_max_y
        self.apple_size = apple_pixel_size
        self.screen = screen 
        self.spawned = False 
        
    def get_apple_position(self):
        return {"x":self.apple_x,"y":self.apple_y}

    def spawn(self):        
        self.apple_x = random.randrange(0,self.grid_max_x) * self.apple_size
        self.apple_y = random.randrange(0,self.grid_max_y) * self.apple_size 

    def draw(self):
        pygame.draw.rect(self.screen, self.apple_colour,(self.apple_x,self.apple_y,self.apple_size,self.apple_size))

class Snake():
    def __init__(self,screen,snake_colour,width,height,apple):
        self.screen = screen
        self.screen_width = width 
        self.screen_height = height  

        self.snake_x = (self.screen_width - 40) / 2
        self.snake_y = 0 
        self.snake_body = []

        self.snake_colour = snake_colour
        self.snake_pixel_size = 40 
        self.direction = ""
        self.apple = apple 
        self.score = 0 
        self.head_position = (self.snake_x,self.snake_y,self.snake_pixel_size,self.snake_pixel_size)
    def change_direction(self,direction):
        self.direction = direction 
 

    def move(self):
        # change the x and y coordinates based on movements given 
        if self.direction == "UP":
            self.snake_y -= self.snake_pixel_size 
        if self.direction == "DOWN":
            self.snake_y += self.snake_pixel_size 
        if self.direction == "LEFT":
            self.snake_x -= self.snake_pixel_size 
        if self.direction  == "RIGHT":
            self.snake_x += self.snake_pixel_size 

    def collided(self):
        if self.snake_x > self.screen_width or self.snake_x < 0:
            return True  
        if self.snake_y > self.screen_height or self.snake_y < 0:
            return True  
        
        # collided with the apple 
        if self.snake_x == self.apple.get_apple_position()["x"]  and self.snake_y == self.apple.get_apple_position()["y"]:
            print("nom")
            self.grow()
            self.apple.spawn()

        else:
            return False

    def grow(self):
        self.snake_body.insert(0,self.head_position)


    def draw(self):
        self.head_position = (self.snake_x,self.snake_y,self.snake_pixel_size,self.snake_pixel_size)
        self.snake_body.insert(0,self.head_position) # insert the new head position 
        
        for body in self.snake_body: # draw the entire snake 
            pygame.draw.rect(self.screen,self.snake_colour,body)

        # remove the tail so all the values are updated 
        self.snake_body.remove(self.snake_body[-1]) 


class Snake_Game():
    def __init__(self):
        self.screen_width = 840 
        self.screen_height = 840 
        
        self.pixel_size = 40 
        self.pixel_grid_max_x = int(self.screen_width / self.pixel_size)
        self.pixel_grid_max_y = int(self.screen_height / self.pixel_size)

        self.red = (255,0,0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.white = (255,255,255)
        self.black = (0,0,0)

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True 

        self.apple = Apple(screen=self.screen,
                           apple_colour=self.green,
                           grid_max_x=self.pixel_grid_max_x,
                           grid_max_y=self.pixel_grid_max_y,
                           apple_pixel_size=self.pixel_size
        )

        self.snake = Snake(
            screen=self.screen,
            snake_colour=self.red,
            width=self.screen_width,
            height=self.screen_height,
            apple=self.apple
        )

    def keypress_events(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                self.snake.change_direction("UP")
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.snake.change_direction("DOWN")
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.snake.change_direction("LEFT")
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.snake.change_direction("RIGHT")


    def checkered_background(self):
        i  = 0 
        for y in range(self.pixel_grid_max_y):
            for x in range(self.pixel_grid_max_x):
                if (i % 2  == 0): # even black odd white
                    colour = self.black
                else:
                    colour = self.white 
                rectangle_position = (y * self.pixel_size,x * self.pixel_size,self.pixel_size,self.pixel_size)
                pygame.draw.rect(self.screen, colour,rectangle_position)
                i += 1


    def start(self):
        while self.running:
            for event in pygame.event.get():
                self.keypress_events(event)
            self.checkered_background()
        
            if self.snake.collided() == True:
                self.running = False 
    
            self.snake.move()
            self.snake.draw()
            self.apple.draw()
            pygame.display.flip()
            self.clock.tick(15)  # FPS

Snake_Game().start()