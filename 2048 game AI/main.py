from env import *
import display
import pygame

game = Game()

game.reset()
info = display.init((300,300))
FPS = 1
clock = pygame.time.Clock()
run = True
while run:
    action = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    action = 0
                case pygame.K_DOWN:
                    action = 2
                case pygame.K_LEFT:
                    action = 3
                case pygame.K_RIGHT:
                    action = 1
    if action != None:
        game.play_step(action)
        display.render(0,game.grid,info)

    clock.tick(FPS)
display.quite()