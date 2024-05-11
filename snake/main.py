import pygame 
import random 
import time 
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
text_font = pygame.font.SysFont("Arial",30)




class Snake():
    def __init__(self):
        self.direction = "STATIC" 
        self.snake_y = 0 
        self.snake_x = 400
        self.snake_body = []

    # sets the direction the snake should move in  
    def set_head_direction(self,direction):
        # makes sure the snake cant go back on itself, it can only go forward 
        if direction == "UP" and self.direction == "DOWN" or self.direction == "DOWN" and direction == "UP" or self.direction == "LEFT" and direction == "RIGHT" or self.direction == "RIGHT" and direction == "LEFT":
            return 
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
        print("grow")
        self.snake_body.insert(0,(self.snake_x,self.snake_y,pixel_size,pixel_size))

    def draw(self):
        self.snake_body.insert(0,(self.snake_x,self.snake_y,pixel_size,pixel_size))
        if len(self.snake_body) > 1:
            self.snake_body.remove(self.snake_body[-1]) 
    
        for body in self.snake_body: # draw the entire snake 
            pygame.draw.rect(screen,green,body)


    def body(self):
        return self.snake_body 
        

class Apple():
    def __init__(self):
        self.apple_x = 0 
        self.apple_y = 0 
        self.apples_eaten = 0 
        self.random_apple()
    def random_apple(self):
        self.apple_x = random.randrange(0,pixel_grid_max_x) * pixel_size
        self.apple_y = random.randrange(0,pixel_grid_max_y) * pixel_size
        

    def eat(self):
        # add +1 to counter and randomise the next apple position
        self.apples_eaten += 1 
        self.random_apple()    
    def eaten(self):
        return self.apples_eaten

    def spawn(self):
        pygame.draw.rect(screen,red,(self.apple_x,self.apple_y,pixel_size,pixel_size))

    def position(self):
        return {"x":self.apple_x,"y":self.apple_y}
    

    
class Snake_Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True 
        self.time_start = time.time()

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
    
    def stats(self):
        # current time 
        # current score 
        elapsed =  round(time.time() - self.time_start)  
        score = self.apple.eaten()

        img = text_font.render(f"time: {elapsed}s",True,red)
        img2 = text_font.render(f"score: {score}",True,red)

        screen.blit(img,(screen_width - pixel_size * 2.5,0))
        screen.blit(img2,(screen_width - pixel_size * 2.5,pixel_size))

        
    def game_over():
        pass 

    def check_collision(self):
        # if snake touches snake 
        # if snake touches border of game
        # if snake touches apple 
        apple_position = self.apple.position() 
        snake_body = self.snake.body()
        snake_head = snake_body[0]
        print(snake_body)
        if snake_head[0] == apple_position["x"] and snake_head[1] == apple_position["y"]:
            print("head collision with apple detected")
            self.apple.eat()
            self.snake.grow()

        if snake_head[0] == screen_height or snake_head[1] == screen_width or snake_head[0] < 0 or snake_head[1] < 0:
            print("head collision with border of game detected")
            self.running = False 

        if snake_head in snake_body[2:]:
            print("snake head hit its body")
            self.running = False 


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
            self.stats()

            pygame.display.flip()
            self.clock.tick(15)  # FPS

Snake_Game().start()