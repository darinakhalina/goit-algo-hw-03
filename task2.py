import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 2 / 3**0.5)
    t.pendown()
    t.color("blue")

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()


def main():
    order = 0
    while order not in range(1, 6):
        try:
            order = int(input("Enter the recursion level (integer from 1 to 5): "))
        except ValueError:
            print("Please enter a valid integer.")

    draw_koch_snowflake(order)


if __name__ == "__main__":
    main()
