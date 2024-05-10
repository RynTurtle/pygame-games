import pygame 
import random 
screen_width = 840 
screen_height = 840 
pixel_size = 40 
pixel_grid_max_x = int(screen_width / pixel_size)
pixel_grid_max_y = int(screen_height / pixel_size)
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))




class Snake():
    def __init__(self):
        self.direction = "STATIC" 
        self.snake_y = 0 
        self.snake_x = 400
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
        if len(self.snake_body) == 0:
            return [self.head_position] 
        else:
            return self.snake_body 
        

class Apple():
    def __init__(self):
        self.apple_x = 0 
        self.apple_y = 0 
        self.apples_eaten = 0 

    def eat(self):
        # add +1 to counter and randomise the next apple position
        self.apples_eaten += 1 
        self.apple_x = random.randrange(0,pixel_grid_max_x) * pixel_size
        self.apple_y = random.randrange(0,pixel_grid_max_y) * pixel_size
        

    def spawn(self):
        pygame.draw.rect(screen,red,(self.apple_x,self.apple_y,pixel_size,pixel_size))

    def position(self):
        return {"x":self.apple_x,"y":self.apple_y}
    

    
class Snake_Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True 

        self.snake = Snake()
        self.apple = Apple()
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


    def game_over():
        pass 

    def check_collision(self):
        # if snake touches snake 
        # if snake touches border of game
        # if snake touches apple 
        apple_position = self.apple.position() 

        snake_body = self.snake.body()
        snake_head = snake_body[0]
        if snake_head[0] == apple_position["x"] and snake_head[1] == apple_position["y"]:
            print("head collision with apple detected")

        if snake_head[0] > screen_height or snake_head[1] > screen_width or snake_head[0] < 0 or snake_head[1] < 0:
            print("head collision with border of game detected")

        if len(snake_body) > 1:
            for parts in snake_body:
                body_part_x = parts[0] 
                body_part_y = parts[1]
                if snake_head[0] == body_part_x and snake_head[1] == body_part_y:
                    print("head collision with body detected")




    def checkered_background(self):
        i  = 0 
        for y in range(pixel_grid_max_y):
            for x in range(pixel_grid_max_x):
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
            self.apple.spawn()
            self.check_collision()


            pygame.display.flip()
            self.clock.tick(15)  # FPS

Snake_Game().start()