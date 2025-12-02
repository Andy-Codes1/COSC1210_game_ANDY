import pygame
import os 
# OS is used to interact with operating system and work around directories

# Grid and Room Settings
# Number is Pixels
TILE_SIZE = 64 
GRID_ROWS = 8
GRID_COLS = 8
ROOM_WIDTH = TILE_SIZE * GRID_ROWS
ROOM_HEIGHT = TILE_SIZE * GRID_COLS
WALL_THICK = 4
MINES = 10
TITLE = "MINESWEEPER"

# Screen Size
WIDTH = ROOM_WIDTH * GRID_COLS
HEIGHT = ROOM_HEIGHT * GRID_ROWS

# Colors (R, G, B)
BG_COLOR = (20, 20, 24)
WALL_COLOR = (200, 200, 200)
PLAYER_COLOR = (100, 200, 255)
BOX_COLOR = (225,153,100)

# Frames Per Second
FPS = 60

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "Assets")

# initialize pygame (needed before some image/transform ops)
pygame.init()

# Intialize empty list of tile numbers starting at 1 and ending before 9
# Then use a for loop to append all tile pngs into the game all at once
tile_numbers = []
for i in range(1,9):
    path = os.path.join(ASSETS_DIR, f"Clue{i}.png")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing asset: {path}")
    tile_numbers.append(pygame.transform.scale(pygame.image.load(path), (TILE_SIZE, TILE_SIZE)))


# Using transfrom and scale from pygame to load in correctly sized images
tile_empty = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "tile_5.png")), (TILE_SIZE, TILE_SIZE))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "tile_38.png")), (TILE_SIZE, TILE_SIZE))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "flagged.png")), (TILE_SIZE, TILE_SIZE))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "bomb.png")), (TILE_SIZE, TILE_SIZE))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "Brick1.png")), (TILE_SIZE, TILE_SIZE))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join(ASSETS_DIR, "notbomb.png")), (TILE_SIZE, TILE_SIZE))
