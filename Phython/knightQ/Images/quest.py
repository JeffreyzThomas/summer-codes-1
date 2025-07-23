########## 1.3 ##########
import pgzrun # imports the pgzrun module
# Define the height & width of the game window, & the size of each
GRID_WIDTH = 16 # The game board is 16 tiles wide
GRID_HEIGHT = 12 # The game board is 12 tiles tall
GRID_SIZE = 50 # Each tile is 50 by 50 pixels
# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
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
# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# This function converts a grid position to screen coordinates
def DrawBackground():
    for y in range (GRID_HEIGHT): # loop over each grid row
        for x in range (GRID_WIDTH): # loop over each grid column
            screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named imaged at the given screen position
def SetupGame():
    global player
    playeer = pgzrun.Actor("player", anchor=("left", "top"))
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
# draw() is
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
pgzrun.go() 