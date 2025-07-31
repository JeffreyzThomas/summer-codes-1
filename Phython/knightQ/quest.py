import pgzrun

# Smaller grid
GRID_WIDTH = 24
GRID_HEIGHT = 20
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

# Guard move interval slowed down
GUARDMOVEINTERVAL = 0.1

# Smaller map to fit screen
MAP = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W W W   G  WWW  W W W  W",
    "W W WWWWWWWW     W W  KW",
    "W W   G         WWW W  W",
    "W WWWWWWWWWWW WW   W W W",
    "W   W     W   WW W W W W",
    "WWW                    W",
    "W                      W",
    "W WWWWW W W W WW W WWWWW",
    "W W          PW  W  G  W",
    "W W WWWWW W WWWWWWW WWWW",
    "W W       W          W W",
    "W WWWWWWWWW WWWWWWWW W W",
    "W     G.               W",
    "W              ww      W",
    "WWWWWWWWWWWWWWWWWWWWWWWWW"
]

def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def DrawBackground():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y))

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))

def SetupGame():
    global gameOver, player, keysToCollect, guards
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    gameOver = False

    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)

def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))

def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()

def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()

def MovePlayer(dx, dy):
    global gameOver
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W":
        return
    elif square == "D":
        if len(keysToCollect) > 0:
            return
        else:
            gameOver = True
    for key in keysToCollect:
        (keyX, keyY) = GetActorGridPos(key)
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break
    player.pos = GetScreenCoords(x, y)

def MoveGuard(guard):
    global gameOver
    if gameOver:
        return

    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)

    dx, dy = 0, 0

    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        dx = 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        dx = -1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        dy = 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        dy = -1

    newX, newY = guardX + dx, guardY + dy
    guard.pos = GetScreenCoords(newX, newY)

    if (newX, newY) == (playerX, playerY):
        gameOver = True

def MoveAllGuards():
    for guard in guards:
        MoveGuard(guard)

def on_key_down(key):
    if gameOver:
        if key == keys.R:
            SetupGame()
        return
    if key == keys.LEFT:
        MovePlayer(-1, 0)
    elif key == keys.UP:
        MovePlayer(0, -1)
    elif key == keys.RIGHT:
        MovePlayer(1, 0)
    elif key == keys.DOWN:
        MovePlayer(0, 1)

def DrawGameOver():
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    screen.draw.text("GAME OVER!", center=screenMiddle, fontsize=60, color="red")
    screen.draw.text("Press R to Restart", center=(WIDTH / 2, HEIGHT / 2 + 50), fontsize=40, color="white")

SetupGame()
clock.schedule_interval(MoveAllGuards, GUARDMOVEINTERVAL)
pgzrun.go()
  