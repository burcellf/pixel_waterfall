import pygame, sys, pymunk
import numpy as np


def create_water(space):
    #               mass, inertia
    body = pymunk.Body(1, 100, body_type = pymunk.Body.DYNAMIC) # moving body
    rd_y = np.random.randint(-9000, 0)
    rd_x = np.random.randint(55, 135)
    
    body.position = (400+rd_x, 0+rd_y)
    shape = pymunk.Circle(body, 1) # (body, radius/shape)
    space.add(body, shape) # creates an invisible 'force' for the body
    
    return shape # returning the shape to pygame allows us to turn invisible force into water


def draw_water_drop(water_drop):
    
    for water in water_drop:
        pos_x = int(water.body.position.x)
        pos_y = int(water.body.position.y)
        
        # draw each water_drop on screen, with color, originating at this position, radius
        pygame.draw.circle(screen, (0, 180, 225), (pos_x, pos_y), 1)
        

def static_ball(space):
    
    body = pymunk.Body(body_type = pymunk.Body.STATIC) # unmoving body
    body.position = (500, 500)
    
    shape = pymunk.Circle(body, 50) # (body, radius)
    space.add(body, shape) # creates an invisible 'force' for the body
    return shape # returning the shape to pygame allows us to turn invisible force into a ball


def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        # draw each ball on screen, with color, originating at this position, radius
        # pygame.draw.circle(screen, (130, 0, 60), (pos_x, pos_y), 50) # ball with color
        pygame.draw.circle(screen, (27, 27, 27), (pos_x, pos_y), 50) # invisible ball


pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
space = pymunk.Space()

#               (x,  y)
space.gravity = (0, 150)

water_drop = []
for i in range(3000):
    water_drop.append(create_water(space))

balls = []
balls.append(static_ball(space))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((27, 27, 27))
    
    draw_water_drop(water_drop)
    draw_static_ball(balls)
    
    space.step(1/175)
    pygame.display.update() # rendering the frame
    clock.tick(240) # 120fps
