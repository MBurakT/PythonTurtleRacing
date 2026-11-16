import turtle
import random
import time


def get_number_of_racers() -> int:
    racers = 0
    while True:
        racers = input("Enter the number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Numbers must be in between 2-10! Try again.")
                continue
        else:
            print("Invalid input! Try again.")


def init_turtle_screen(width: int, height: int) -> None:
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title("Turtle Racing")


def create_turtles(colors: list, width: int, height: int) -> list:
    turtles = []
    spacingx = width // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(- width // 2 + (i+1) * spacingx, -height // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors: list, turtles: list, height: int) -> str:
    while True:
        for i, racer in enumerate(turtles):
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()

            if y >= height // 2 - 10:
                return colors[i]


def play() -> None:

    WIDTH, HEIGHT = 500, 500
    COLORS = ["red", "green", "blue", "orange", "yellow",
              "black", "purple", "pink", "brown", "cyan"]

    racers = get_number_of_racers()
    init_turtle_screen(WIDTH, HEIGHT)

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    turtles = create_turtles(colors, WIDTH, HEIGHT)

    answer = input(
        "Type the color of turtle you guess to win the race: ").lower()

    winners_color = race(colors, turtles, HEIGHT)

    print(f"Winner is {winners_color} turtle!")

    if answer == winners_color:
        print("Congrulations! You win.")
    else:
        print("Wrong! You lose.")

    time.sleep(5)


play()
