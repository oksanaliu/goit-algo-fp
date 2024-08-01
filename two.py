import turtle
import math

def draw_branch(length, angle, depth):
    if depth > 0:
        # Малюємо гілку
        turtle.forward(length)

        # Малюємо праву підгілку
        turtle.right(angle)
        draw_branch(length * math.cos(math.radians(angle)), angle, depth - 1)

        # Повертаємося до початкового положення
        turtle.left(2 * angle)
        draw_branch(length * math.cos(math.radians(angle)), angle, depth - 1)

        # Повертаємося до виходу
        turtle.right(angle)
        turtle.backward(length)

def setup_turtle():
    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -turtle.Screen().window_height() // 2 + 50)
    turtle.pendown()
    turtle.speed(0)
    turtle.color("black")

def main():
    # Отримання рівня рекурсії від користувача
    recursion_level = int(input("Введіть рівень рекурсії для дерева: "))

    # Налаштування екрану
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Налаштування черепахи
    setup_turtle()

    # Малювання дерева
    draw_branch(100, 30, recursion_level)

    # Завершення роботи
    turtle.done()

if __name__ == "__main__":
    main()