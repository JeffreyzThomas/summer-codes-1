import pgzrun  # Pygame Zero

# Game grid and size
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

# Game map
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWWWWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]

# Convert grid coordinates to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

# Draw background tiles (floor)
def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

# Draw static objects like walls and doors
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            pos = GetScreenCoords(x, y)
            if square == "W":
                screen.blit("wall", pos)
            elif square == "D":
                screen.blit("door", pos)

# Initialize game
def SetupGame():
    global player, player_grid_pos
    player = Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if MAP[y][x] == "P":
                player_grid_pos = [x, y]
                player.pos = GetScreenCoords(x, y)
                break

# Check if the tile is walkable
def CanMoveTo(x, y):
    if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
        return MAP[y][x] not in ("W")
    return False

# Update player position based on key input
def update():
    dx, dy = 0, 0
    if keyboard.left:
        dx = -1
    elif keyboard.right:
        dx = 1
    elif keyboard.up:
        dy = -1
    elif keyboard.down:
        dy = 1

    if dx != 0 or dy != 0:
        new_x = player_grid_pos[0] + dx
        new_y = player_grid_pos[1] + dy
        if CanMoveTo(new_x, new_y):
            player_grid_pos[0] = new_x
            player_grid_pos[1] = new_y
            player.pos = GetScreenCoords(new_x, new_y)

# Draw everything on screen
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    player.draw()

# Start the game
SetupGame()
pgzrun.go()

