
import tkinter as tk
import random

# =========================
# GAME SETTINGS
# =========================

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

SPEED = 200

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("🐍 Snake Game")
root.resizable(False, False)

# Score
score = 0
direction = "Right"
game_over = False

# =========================
# CANVAS
# =========================

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="black"
)
canvas.pack()

# =========================
# SNAKE
# =========================

snake = [
    [300, 200],
    [280, 200],
    [260, 200]
]

# =========================
# FOOD
# =========================

food = [
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
]

# =========================
# DRAW GAME
# =========================

def draw_game():

    canvas.delete("all")

    # Draw snake
    for i, segment in enumerate(snake):

        if i == 0:
            canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + CELL_SIZE,
                segment[1] + CELL_SIZE,
                fill="lime",
                outline="white"
            )
        else:
            canvas.create_rectangle(
                segment[0],
                segment[1],
                segment[0] + CELL_SIZE,
                segment[1] + CELL_SIZE,
                fill="green",
                outline="black"
            )

    # Draw food
    canvas.create_oval(
        food[0],
        food[1],
        food[0] + CELL_SIZE,
        food[1] + CELL_SIZE,
        fill="red",
        outline="white"
    )

    # Score
    canvas.create_text(
        60,
        20,
        text=f"Score: {score}",
        fill="white",
        font=("Arial", 16, "bold")
    )


# =========================
# CHANGE DIRECTION
# =========================

def change_direction(new_direction):

    global direction

    if new_direction == "Up" and direction != "Down":
        direction = "Up"

    elif new_direction == "Down" and direction != "Up":
        direction = "Down"

    elif new_direction == "Left" and direction != "Right":
        direction = "Left"

    elif new_direction == "Right" and direction != "Left":
        direction = "Right"


# =========================
# KEYBOARD
# =========================

root.bind(
    "<Up>",
    lambda event: change_direction("Up")
)

root.bind(
    "<Down>",
    lambda event: change_direction("Down")
)

root.bind(
    "<Left>",
    lambda event: change_direction("Left")
)

root.bind(
    "<Right>",
    lambda event: change_direction("Right")
)


# =========================
# GAME LOOP
# =========================

def game_loop():

    global food
    global score
    global game_over

    if game_over:
        return

    # Current head
    head = snake[0].copy()

    # Move snake
    if direction == "Up":
        head[1] -= CELL_SIZE

    elif direction == "Down":
        head[1] += CELL_SIZE

    elif direction == "Left":
        head[0] -= CELL_SIZE

    elif direction == "Right":
        head[0] += CELL_SIZE

    # =====================
    # WALL COLLISION
    # =====================

    if (
        head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
    ):
        end_game()
        return

    # =====================
    # BODY COLLISION
    # =====================

    if head in snake:
        end_game()
        return

    # Add new head
    snake.insert(0, head)

    # =====================
    # FOOD COLLISION
    # =====================

    if head == food:

        score += 10

        # Generate new food
        while True:

            new_food = [
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            ]

            if new_food not in snake:
                food = new_food
                break

    else:
        # Remove tail
        snake.pop()

    draw_game()

    # Continue game
    root.after(SPEED, game_loop)


# =========================
# GAME OVER
# =========================

def end_game():

    global game_over

    game_over = True

    canvas.create_rectangle(
        150,
        140,
        450,
        260,
        fill="black",
        outline="red",
        width=3
    )

    canvas.create_text(
        300,
        180,
        text="GAME OVER!",
        fill="red",
        font=("Arial", 28, "bold")
    )

    canvas.create_text(
        300,
        220,
        text=f"Final Score: {score}",
        fill="white",
        font=("Arial", 18, "bold")
    )

    canvas.create_text(
        300,
        245,
        text="Close the window to exit",
        fill="white",
        font=("Arial", 11)
    )


# =========================
# START
# =========================

draw_game()
game_loop()

root.mainloop()

