# adventure_functions.py
import os
import pygame
import Settings as config





def draw_room(screen, row, col):
    left = col * config.ROOM_WIDTH
    right = left + config.ROOM_WIDTH
    top = row * config.ROOM_HEIGHT
    bottom = top + config.ROOM_HEIGHT
    mid_x = (left + right) // 2
    mid_y = (top + bottom) // 2

    # Top wall
    if row == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (right, top), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (mid_x - config.DOOR_SIZE // 2, top), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (mid_x + config.DOOR_SIZE // 2, top), (right, top), config.WALL_THICK)

    # Bottom wall
    if row == config.GRID_ROWS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (left, bottom), (right, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, bottom), (mid_x - config.DOOR_SIZE // 2, bottom), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (mid_x + config.DOOR_SIZE // 2, bottom), (right, bottom), config.WALL_THICK)

    # Left wall
    if col == 0:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (left, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (left, top), (left, mid_y - config.DOOR_SIZE // 2), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (left, mid_y + config.DOOR_SIZE // 2), (left, bottom), config.WALL_THICK)

    # Right wall
    if col == config.GRID_COLS - 1:
        pygame.draw.line(screen, config.WALL_COLOR, (right, top), (right, bottom), config.WALL_THICK)
    else:
        pygame.draw.line(screen, config.WALL_COLOR, (right, top), (right, mid_y - config.DOOR_SIZE // 2), config.WALL_THICK)
        pygame.draw.line(screen, config.WALL_COLOR, (right, mid_y + config.DOOR_SIZE // 2), (right, bottom), config.WALL_THICK)


def is_blocked(x, y):
    """Return True if the player is hitting a wall (excluding doors)"""
    for row in range(config.GRID_ROWS):
        for col in range(config.GRID_COLS):
            left = col * config.ROOM_WIDTH
            right = left + config.ROOM_WIDTH
            top = row * config.ROOM_HEIGHT
            bottom = top + config.ROOM_HEIGHT
            mid_x = (left + right) // 2
            mid_y = (top + bottom) // 2

            if left <= x <= right and top <= y <= bottom:
                if x - config.PLAYER_RADIUS < left:
                    if col == 0 or not (mid_y - config.DOOR_SIZE//2 <= y <= mid_y + config.DOOR_SIZE//2):
                        return True
                if x + config.PLAYER_RADIUS > right:
                    if col == config.GRID_COLS - 1 or not (mid_y - config.DOOR_SIZE//2 <= y <= mid_y + config.DOOR_SIZE//2):
                        return True
                if y - config.PLAYER_RADIUS < top:
                    if row == 0 or not (mid_x - config.DOOR_SIZE//2 <= x <= mid_x + config.DOOR_SIZE//2):
                        return True
                if y + config.PLAYER_RADIUS > bottom:
                    if row == config.GRID_ROWS - 1 or not (mid_x - config.DOOR_SIZE//2 <= x <= mid_x + config.DOOR_SIZE//2):
                        return True
                return False

    return True

def draw_obstacle(screen):
    '''draws a simple box'''
    left = 10
    top = 10
    right = 20
    bottom = 20
    pygame.draw.line(screen, config.BOX_COLOR, (left, top), (right, top), config.WALL_THICK)
    pygame.draw.line(screen, config.BOX_COLOR, (left, bottom), (right, bottom), config.WALL_THICK)
    pygame.draw.line(screen, config.BOX_COLOR, (right, top), (right, bottom), config.WALL_THICK)
    pygame.draw.line(screen, config.BOX_COLOR, (left, top), (left, bottom), config.WALL_THICK)


_player_image = None
_warned_once = False

def load_player_image():
    """Call once at startup after pygame.init()."""
    global _player_image, _warned_once
    _player_image = None  # default

    path = getattr(config, "PLAYER_IMAGE_PATH", None)
    size = getattr(config, "PLAYER_IMAGE_SIZE", None)

    if path and os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        _player_image = img
    else:
        if not _warned_once:
            print("No player image found or PLAYER_IMAGE_PATH not set; using circle.")
            _warned_once = True

def draw_player(screen, x, y):
    """Draw sprite centered at (x, y); fall back to circle if no image."""
    if _player_image:
        rect = _player_image.get_rect(center=(int(x), int(y)))
        screen.blit(_player_image, rect.topleft)
    else:
        pygame.draw.circle(screen, config.PLAYER_COLOR, (int(x), int(y)), config.PLAYER_RADIUS)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), config.PLAYER_RADIUS, 2)

# --- Mines / bombs helpers ---
import random


def get_cell_for_coords(x, y):
    """Return (row, col) for pixel coordinates (x, y), clamped to grid."""
    col = int(x // config.ROOM_WIDTH)
    row = int(y // config.ROOM_HEIGHT)
    col = max(0, min(config.GRID_COLS - 1, col))
    row = max(0, min(config.GRID_ROWS - 1, row))
    return row, col


def place_mines(num_mines=10, rows=None, cols=None):
    """Return a set of (row, col) tuples with randomly placed mines.

    - If num_mines >= total cells, all cells become mines.
    - Uses random.sample for non-overlapping placement.
    """
    if rows is None:
        rows = config.GRID_ROWS
    if cols is None:
        cols = config.GRID_COLS

    total = rows * cols
    num = max(0, min(num_mines, total))

    all_cells = [(r, c) for r in range(rows) for c in range(cols)]
    chosen = set(random.sample(all_cells, num)) if num > 0 else set()
    return

# copy and paste this code to the end of the adventure_functions.py file
# add show_game_over to the list of imported functions
# add show_game_over(screen) as part of the sentinel control
def show_game_over(screen):
    """Draw a Game Over box in the center of the screen."""
    font = pygame.font.Font(None, 72)  # default font, large size
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2))

    # Draw a semi-transparent dark box behind the text
    box_width = text_rect.width + 40
    box_height = text_rect.height + 40
    box_surface = pygame.Surface((box_width, box_height))
    box_surface.set_alpha(180)  # transparency
    box_surface.fill((0, 0, 0))
    box_rect = box_surface.get_rect(center=text_rect.center)

    # Blit box then text
    screen.blit(box_surface, box_rect)
    screen.blit(text, text_rect)
    pygame.display.flip()

    # Pause to let player see the message
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False

# Tile Types for 2D board
# "B" = Bomb
# "E" = Empty Square
# "C" = Clue Square
# "X" = Unknown Square
class Tile: 
    # so basically I am making a class for Tiles, x coordinate, y cordinate, and the type as parameter. I'm making revealed and flagged as false because they are not true yet
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        #now I am setting self.x and y to a box which is why it's 70/8 multiplied by the x value 
        self.x = x * (70 / 8)
        self.y = y * (70 / 8)
        self.image = image
        self.type = type
        self.revealed = revealed 
        self.flagged = flagged
    
    def square(self, board_surface):
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y)) #in Pygame the code blit puts something ontop of another thing, x,y are used for the squares to put image above the square
        elif self.flagged and not self.revealed: 
            board_surface.blit(self.flagged, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(self.unknown, (self.x, self.y))


#def mine_location_dictionary(Total_bombs):
 #   Location_Bombs = {}
 #   for ix in GRID_ROWS:
 #       for iy in GRID_COLS:
 #           if Bombs.type == "B":
  #              Location_Bombs.append(ix, iy)
 #   print(Location_Bombs)
    #To see a 2D model of all bombs and their locations. 
                
        
