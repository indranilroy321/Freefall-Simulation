import pygame           
import random                             

class Balls:                                                                   #8
    def __init__(self, color, center_x, center_y, radius, width):              #8        
        self.color = color
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.width = width
        self.center_y_incr = .1

    def draw_ball(self, screen,color, center_x, center_y, radius, width):      #8
        pygame.draw.circle(screen, color, [center_x, center_y], radius, width)

def create_balls(screen, ball, no_of_balls):                                   #9
    for i in range(no_of_balls):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        radius = random.randint(10, 60)
        center_x = random.randint(1, page_width - radius)        
        center_y = radius
        b = Balls(color, center_x, center_y, radius, 0)
        ball.append(b)
    
    return ball

# Driver Code                                                   

page_width, page_depth = 1600, 820                               

pygame.init()                                                   
screen = pygame.display.set_mode((page_width, page_depth))      
pygame.display.set_caption("Free Fall Simulation")              

radius = 80                                                     
border_width = 0        
ball = []                                                       #9
no_of_balls = 100                                                #9
ball = create_balls(screen, ball, no_of_balls)                  #9

clock=pygame.time.Clock()                                      

running = True                                                  

while running:                    
    clock.tick(100)                                         

    screen.fill((0, 0, 0))                                      

    for event in pygame.event.get():                            
        if event.type == pygame.QUIT:                           
            running = False     

    for i in range(len(ball)):                                                                          #11
        ball[i].center_y = ball[i].radius + ball[i].center_y_incr                                       #12
        ball[i].draw_ball(screen, ball[i].color, ball[i].center_x, ball[i].center_y, ball[i].radius, 0) #11
        if ball[i].center_y <= page_depth - (ball[i].radius * 2):
            r = 1 + random.randint(1, 10) / 100
            ball[i].center_y_incr = ball[i].center_y_incr * r     # 1.05
        else:
            ball[i].center_y_incr = page_depth - (ball[i].radius * 2)

    pygame.display.flip()                                       

pygame.display.update()                                         