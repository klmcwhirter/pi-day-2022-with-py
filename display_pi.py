'''
Usage: display_pi [--palette COLORS] [--num-digits N] [--width W] [--height H] [--help] [--version]

Options:
    --palette COLORS    where COLORS is a comma separated list of color names representing digits 0-9 [default: black,crimson,red,orange,yellow,green,lightblue,blue,violet,purple]
    --num-digits N      the number of digits of PI to display [default: 100_000]

    --width W           the width of the display [default: 900]
    --height H          the height of the display [default: 900]

    --help              display this help text and exit
    --version           display version and exit
'''
import turtle
from math import pi

from docopt import docopt

'''Pre-calculate possible angles to turn per pi digit'''
circle_angles = list((x + 1) * 36 for x in range(10))


def pi_digit_generator(num_digits):
    '''from https://stackoverflow.com/questions/9004789/1000-digits-of-pi-in-python'''
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(num_digits):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


class PiDisplayAdapter:
    def __init__(self, opts):
        self.palette = [c for c in opts['--palette'].split(',')]
        self.num_digits = int(opts['--num-digits'])

        self.width = int(opts['--width'])
        self.height = int(opts['--height'])

    def display_pi(self):
        turtle.title(f'Happy PI day! 2022')
        turtle.setup(self.width, self.height)
        turtle.speed(0)
        turtle.delay(0)
        turtle.up()
        turtle.goto(-(self.width / 2) + 100, 100)
        turtle.setheading(0)
        turtle.down()
        turtle.hideturtle()
        turtle.pensize(1)

        self.draw_with_pi()

        turtle.done()

    def draw_with_pi(self):
        for digit in pi_digit_generator(self.num_digits):
            self.left_circle_stroke(digit)
        self.show_done()

    def left_circle_stroke(self, n):
        color = self.palette[n]
        # print(f'color={color}')
        turtle.pencolor(color)
        turtle.forward(n)
        turtle.left(circle_angles[n])

    def show_done(self):
        turtle.penup()
        turtle.goto(200, 0)
        turtle.pencolor('red')
        turtle.write('Python Turtle drawing', font=('Arial', '16', 'bold'))
        turtle.penup()
        turtle.goto(240, -20)
        turtle.write(f'with {self.num_digits} digits of PI', font=('Arial', '12', 'bold'))
        turtle.bgcolor("black")


def display_pi(opts):
    adapter = PiDisplayAdapter(opts)
    adapter.display_pi()


if __name__ == '__main__':
    opts = docopt(__doc__, version=str(pi))
    print(opts)

    display_pi(opts)
