import pygame
import sys

pygame.init()

# Grid constants
GRID_SIZE = 50
GRID_WIDTH = 10
GRID_HEIGHT = 8
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 200, 0)

font = pygame.font.SysFont(None, 40)

# Smaller map
MAP = [
    "WWWWWWWWWW",
    "WP     G W",
    "W WWWW W W",
    "W   W    W",
    "W W W WWWW",
    "W W   W  W",
    "W   G   KW",
    "WWWWWWWWWW"
]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze with Guards")

def draw_map():
    for y, row in enumerate(MAP):
        for x, char in enumerate(row):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if char == "W":
                pygame.draw.rect(screen, GRAY, rect)
            elif char == "G":
                pygame.draw.rect(screen, RED, rect)
            elif char == "K":
                pygame.draw.rect(screen, YELLOW, rect)
            elif char == "P":
                pygame.draw.rect(screen, BLUE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

def find_positions(char):
    return [(x, y) for y, row in enumerate(MAP) for x, c in enumerate(row) if c == char]

def move_player(dx, dy):
    global won, game_over
    px, py = find_positions("P")[0]
    new_x, new_y = px + dx, py + dy
    if MAP[new_y][new_x] not in ("W"):
        if MAP[new_y][new_x] == "K":
            won = True
        elif MAP[new_y][new_x] == "G":
            game_over = True
        row = list(MAP[py])
        row[px] = " "
        MAP[py] = "".join(row)
        row = list(MAP[new_y])
        row[new_x] = "P"
        MAP[new_y] = "".join(row)

def move_guards():
    global game_over
    guards = find_positions("G")
    player = find_positions("P")[0]
    new_map = [list(row) for row in MAP]
    for gx, gy in guards:
        dx = player[0] - gx
        dy = player[1] - gy
        move_x, move_y = gx, gy
        if abs(dx) > abs(dy):
            move_x += 1 if dx > 0 else -1
        elif dy != 0:
            move_y += 1 if dy > 0 else -1
        if MAP[move_y][move_x] in (" ", "P"):
            if MAP[move_y][move_x] == "P":
                game_over = True
            new_map[gy][gx] = " "
            new_map[move_y][move_x] = "G"
    return ["".join(row) for row in new_map]

clock = pygame.time.Clock()
running = True
won = False
game_over = False
guard_timer = 0

while running:
    screen.fill(BLACK)
    draw_map()

    if won:
        text = font.render("You got the key!", True, GREEN)
        screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2))
    elif game_over:
        text = font.render("Caught by a guard!", True, RED)
        screen.blit(text, (WIDTH // 2 - 140, HEIGHT // 2))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won and not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            move_player(-1, 0)
        elif keys[pygame.K_RIGHT]:
            move_player(1, 0)
        elif keys[pygame.K_UP]:
            move_player(0, -1)
        elif keys[pygame.K_DOWN]:
            move_player(0, 1)

        guard_timer += 1
        if guard_timer % 20 == 0:
            MAP = move_guards()

    clock.tick(10)

pygame.quit()
sys.exit()

