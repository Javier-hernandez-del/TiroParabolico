from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
# input realizado para escoger la velocidad en la que el juego estará corriendo.
velocity = float(input("Enter the speed of the balls if 1 is the normal speed: "))

def tap(x, y):  # Función que permite a la bola responder al toque de la pantalla.
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x * velocity + 200) / 25
        speed.y = (y * velocity + 200) / 25

def inside(xy):  # Función que evita que la bola y obtáculos se salgan de la pantalla.
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():  # Función que dibuja la bola y los obstáculos.
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():  # Función que mueve la bola y los obstáculos dependiendo del tiempo escogido.
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

# Fors multiplicados por el parámetro de velocidad escogido por el usuario para hacerlo más rápido.
    for target in targets:
        target.x -= 0.5 * velocity

    if inside(ball):
        speed.y -= 0.35 * velocity
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            # Nuevo target que continua con la velocidad.
            targets[targets.index(target)].x = 200

    ontimer(move, 50)

# Parámetros del juego.
setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()