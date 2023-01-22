import pygame
def init(size):
    info = {}

    pygame.init()
    info['WIN'] = pygame.display.set_mode(size)

    info['DX'] = size[0]/4
    info['DY'] = size[1]/4

    info['fontText'] = pygame.font.Font("freesansbold.ttf", 32)
    info['fontSquare'] = pygame.font.Font("freesansbold.ttf", 20)

    return info


def render(score, grid, info):
    info['WIN'].fill((0, 99, 0))

    # write the score
    msg = info['fontText'].render(str(score),False,(0,0,0),(0, 85, 0))
    msg_rect = msg.get_rect()
    msg_rect.topleft = (0,0)
    
    info['WIN'].blit(msg,msg_rect)

    # draw grid
    for x in range(4):
        for y in range(4):
            square = grid[y][x]
            if square == 0: continue
            pygame.draw.rect(info['WIN'],get_color(square),(x*info['DX'],y*info['DY'],info['DX'],info['DY']))
            msg = info['fontText'].render(str(square),False,(0,0,0),(0, 85, 0))
            msg_rect = msg.get_rect()
            msg_rect.center = (x*info['DX'],y*info['DY'])
    pygame.display.flip()

def quite():
    pygame.quit()

def get_color(n):
    match n:
        case 2:
            return (255, 200, 0)
        case 4:
            return (255, 175, 0)
        case 8:
            return (255, 150, 0)
        case 16:
            return (255, 125, 0)
        case 32:
            return (255, 100, 0)
        case 64:
            return (255, 75, 0)
        case 128:
            return (255, 50, 0)
        case 256:
            return (255, 50, 0)
        case 512:
            return (225, 0, 0)
        case 1024:
            return (150, 0, 0)
        case _:
            return (0, 0, 0)