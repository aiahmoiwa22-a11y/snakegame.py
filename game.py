import pygame
pygame.init()

Clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Space Invaders")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill((0, 0, 0))
    pygame.display.flip()

    Clock.tick(10)


snake = [(10,10), (10,11), (10,12), (10,13), (10,14), (10,15)]
direction = '1,0'

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)
    snake.pop()
    screen.fill((0,0,0))
    
for segment in snake:
        
    cell_size = 20
    cols = 16
    rows = 10
    width = cols * cell_size
    height = rows * cell_size

snake = [(10,10), (10,11), (10,12), (10,13), (10,14), (10,15)]
direction = '1,0'

running = True
while running:
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    snake.insert(0, new_head)
    snake.pop()
    
    screen.fill((0,0,0))
    for x,y in snake:
       rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (0,255,0), rect)
    pygame.display.flip()
    
import random
def place_food(snake, cols, rows):
    while True:
        food = (random.randint(0, cols-1), random.randint(0, rows-1))
        if food not in snake:
            return food
food = place_food(cols, rows)

food_rect = pygame.Rect(food[0] * cell_size, food[1] * cell_size, cell_size, cell_size)
pygame.draw.rect(screen, (255,0,0), food_rect)
pygame.display.flip()

if new_head == food:
    snake.insert(0, new_head)
    food = place_food(cols, rows)
else:
    snake.insert(0, new_head)
    snake.pop()
    
head = snake[0]
new_head = (head[0] + direction[0], head[1] + direction[1])


if new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
    print("Game Over")
    running = False


elif new_head in snake[1:]:
    print("Game Over")
    running = False
    
else:
    if new_head == food:
        snake.insert(0, new_head)
        food = place_food(cols, rows)
    else:
        snake.insert(0, new_head)
        snake.pop()
        
pygame.display.flip()
Clock.tick(20)

pygame.quit()

Clock.tick(20)

pygame.quit()

direction = [1,0]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = [-1,0]
            elif event.key == pygame.K_RIGHT:
                new_direction = [1,0]

                if new_direction and (direction[0] + new_direction[0], direction[1] + new_direction[1]):
                    direction = new_direction
head = snake[0]
new_head = (head[0] + direction[0], head[1] + direction[1])

if new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
    print("Game Over")
    running = False
elif new_head in snake[1:]:
    print("Game Over")
    running = False
else:
    if new_head == food:
        snake.insert(0, new_head)
        food = place_food(cols, rows)
    else:
        snake.insert(0, new_head)
        snake.pop()
pygame.display.flip()
Clock.tick(20)
pygame.quit()

score = len(snake) - 3

font = pygame.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, (255, 255, 255))
screen.blit(score_text, (10, 10))
pygame.display.flip()

base_speed = 5
speed = base_speed + len(snake) // 5
Clock.tick(speed)


fps = 10
Clock.tick(fps)

def show_menu():
    waiting = True
    while waiting:
        screen.fill((0,0,0))
        font = pygame.font.Font(None, 36)
        title_text = font.render("Space Invaders", True, (255,255,255))
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, height // 2 - title_text.get_height() // 2))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False 
                    
    return True
if not show_menu():
    pygame.quit()
    exit()  
    
def show_game_over():
    waiting = True
    while waiting:
        screen.fill((0,0,0))
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Game Over", True, (255,255,255))
        screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.KEYDOWN:
                return True
    return True
                
show_game_over(len(snake) - 3)

obstacles = [(5,5), (5,6), (5,7), (6,5), (6,6), (6,7), (7,5), (7,6), (7,7)]
if new_head in obstacles:
    print("Game Over")
    running = False

for obs in obstacles:
    react = pygame.Rect(obs[0] * cell_size, obs[1] * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, (255,255,255), react)
    
import pygame.mixer
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("eat.wav")
die_sound = pygame.mixer.Sound("die.wav")





