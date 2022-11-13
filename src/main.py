# Complete your game here
# this is raining coin game, it is a update version of asteroids homework
# if we catch the coint, it will gain one point, if we catch the moster, the game will quit
import pygame
from random import randint
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
x = 0
y = height-robot.get_height()
 
coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")
number = 5
positions = []
positions1 = []
for i in range(number):
    positions.append([randint(0,width-coin.get_width()),-randint(100,1000)])

    positions1.append([randint(0,width-coin.get_width()),-randint(100,1000)])    
 
to_right = False
to_left = False
 
points = 0
 
clock = pygame.time.Clock()
 
font = pygame.font.SysFont("Arial", 24)
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
 
        if event.type == pygame.QUIT:
            exit()
 
    if to_right:
        x += 2
    if to_left:
        x -= 2
 
    for i in range(number):
        
        positions1[i][1] += 1
        if positions1[i][1]+monster.get_height() >= y:
            robot_middle = x+robot.get_width()/2
            monster_middle = positions1[i][0]+coin.get_width()/2
            if abs(robot_middle-monster_middle) <= (robot.get_width()+monster.get_width())/2:
                
                positions1[i][0] = randint(0,width-monster.get_width())
                positions1[i][1] = -randint(100,1000)
                exit()
        positions[i][1] += 1
        if positions[i][1]+coin.get_height() >= y:
            robot_middle = x+robot.get_width()/2
            coin_middle = positions[i][0]+coin.get_width()/2
            if abs(robot_middle-coin_middle) <= (robot.get_width()+coin.get_width())/2:
                positions[i][0] = randint(0,width-coin.get_width())
                positions[i][1] = -randint(100,1000)
                points += 1
 
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    for i in range(number):
        screen.blit(coin, (positions[i][0], positions[i][1]))
        screen.blit(monster, (positions1[i][0], positions1[i][1]))
 
    text = font.render("Points: "+str(points), True, (255, 0, 0))
    screen.blit(text, (width-150, 10))
 
    pygame.display.flip()
 
    clock.tick(60)