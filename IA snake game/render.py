import pygame

def init(col,row):
    info = {}

    pygame.init()
    info['WIN'] = pygame.display.set_mode((400,400))

    info['DX'] = 400/col
    info['DY'] = 400/row
    info['col'] = col
    info['row'] = row

    info['fontText'] = pygame.font.Font("freesansbold.ttf", 32)

    return info


def render(action, score, grid, info):
    info['WIN'].fill((0, 99, 0))

    # write the score
    msg = info['fontText'].render(str(score),False,(0,0,0),(0, 85, 0))
    msg_rect = msg.get_rect()
    msg_rect.topleft = (0,0)
    
    info['WIN'].blit(msg,msg_rect)

    # draw grid
    for x in range(info['row']):
        for y in range(info['col']):
            pos = grid[y, x]
            match pos:
                case 1:
                    pygame.draw.rect(info['WIN'],(255,0,0),(x*info['DX'],y*info['DY'],info['DX'],info['DY']))
                case 2:
                    pygame.draw.rect(info['WIN'],(0,255,0),(x*info['DX'],y*info['DY'],info['DX'],info['DY']))
    pygame.display.flip()

def quite():
    pygame.quit()