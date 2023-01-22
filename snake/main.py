import pygame
import random
from snake import Snake

# Initialize Pygame
pygame.init()

# Set the window size
WIDTH = 600
HEIGHT = 600
window_size = (WIDTH,HEIGHT)

# Create the window
WIN = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption('Snake')

# Set grid
rows = 20
columns = 20

grid = [[0 for _ in range(columns)] for _ in range(rows)]

# Calcul size of the case
deltaX = WIDTH/columns
deltaY = HEIGHT/rows

# Place the snake
grid[columns//2][rows//2] = 1
snake = Snake((columns//2,rows//2))

# Place the apple
def placeApple():
    posX = random.randint(0,columns-1)
    posY = random.randint(0,rows-1)
    if grid[posX][posY] != 0:
        placeApple()
    else:
        grid[posX][posY] = 2

placeApple()

fontText = pygame.font.Font("freesansbold.ttf", 32)
def draw():
    # clear the canvas
    WIN.fill((0, 99, 0))

    # write the score
    msg = fontText.render(str(snake.score),False,(0,0,0),(0, 85, 0))
    msg_rect = msg.get_rect()
    msg_rect.topleft = (0,0)
    
    WIN.blit(msg,msg_rect)

    # draw grid
    for x in range(rows):
        for y in range(columns):
            pos = grid[x][y]
            match pos:
                case 1:
                    pygame.draw.rect(WIN,(255,0,0),(x*deltaX,y*deltaY,deltaX,deltaY))
                case 2:
                    pygame.draw.rect(WIN,(0,255,0),(x*deltaX,y*deltaY,deltaY,deltaY))

def update():
    onApple = False

    dir = snake.direction
    pos = snake.positions[-1]
    endTail = snake.positions[0]
    
    match dir:
        case "right":
            newPos = (pos[0] + 1 , pos[1])
        case "left":
            newPos = (pos[0] - 1 , pos[1])
        case "up":
            newPos = (pos[0], pos[1] - 1 )
        case "down":
            newPos = (pos[0], pos[1] + 1 )
    
    # Collision left and right
    if newPos[0] >= columns or newPos[0] < 0:
        pygame.quit()
        exit()
    
    # Collision top and buttom
    if newPos[1] >= rows or newPos[1] < 0:
        pygame.quit()
        exit()
    
    # Collision with the snake
    if grid[newPos[0]][newPos[1]] == 1:
        pygame.quit()
        exit()
    
    snake.positions.append(newPos)
    if grid[newPos[0]][newPos[1]] == 2:
        onApple = True
        snake.score += 1
        placeApple()
    
    grid[newPos[0]][newPos[1]] = 1
    
    if not onApple:
        snake.positions.pop(0)
        grid[endTail[0]][endTail[1]] = 0

# Set FPS
FPS = 3
clock = pygame.time.Clock()

# Run the game loop
running = True
while running:
    # Handle events
    newDir = snake.direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            
            match event.key:
                case pygame.K_UP:
                    newDir = "up" if snake.direction != "down" else "down"
                case pygame.K_DOWN:
                    newDir = "down" if snake.direction != "up" else "up"
                case pygame.K_LEFT:
                    newDir = "left" if snake.direction != "right" else "right"
                case pygame.K_RIGHT:
                    newDir = "right" if snake.direction != "left" else "left"
    
    snake.direction = newDir

    # Update the game state
    update()

    # Draw the game
    draw()
    pygame.display.flip()  # Update the display
    
    clock.tick(FPS)

# Quit Pygame
pygame.quit()