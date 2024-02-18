# importing libraries
import tkinter # note: tkinter is a graphics lib for python
import random

# defining constants
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * ROWS
WINDOW_HEIGHT = TILE_SIZE * COLS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# game window
window = tkinter.Tk()
window.title("SNAKE GAME AHHAHAHAHH")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

# center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format "(w)x(h) + (x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# initialize game
snake = Tile(5*TILE_SIZE, 5*TILE_SIZE) # single tile, snake's head
food = Tile(10*TILE_SIZE, 10*TILE_SIZE)
snake_body = [] # multiple snake tiles
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(event):
    # print(event)
    # print(event.keysym)
    global velocityX, velocityY, game_over

    if (game_over):
        return

    if (event.keysym == "Up" or event.keysym == "w" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (event.keysym == "Down" or event.keysym == "s" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (event.keysym == "Left" or event.keysym == "a" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (event.keysym == "Right" or event.keysym == "d" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score

    if (game_over):
        return
    
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    
    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

    #collision
    if (snake.x == food.x and snake.y == food.y): 
        snake_body.append(Tile(food.x, food.y))
        food.x = random.randint(0, COLS-1) * TILE_SIZE
        food.y = random.randint(0, ROWS-1) * TILE_SIZE
        score += 1

    # update snake body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y


    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE

def draw():
    global snake, food, snake_body, game_over, scoreeeeeeeeeeeeeeeeeee
    move()

    canvas.delete("all")
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "dark red")

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "royal blue")

    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "dark red")

    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "royal blue")

    if (game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "Courier 40", text = f"Game Over: {score}", fill = "white")
    else:
        canvas.create_text(WINDOW_WIDTH/2, 20, font = "Courier 20", text = f"Score: {score}", fill = "white")

    window.after(100, draw) # every 100 ms, recalls function

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()