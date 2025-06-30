import random
import turtle
from turtle import *
from tkinter import *


#Build TKinter window for 'microtransactions'
speed=0.5
revive_price=0.49
paddle_moves=15
AI_enabed=False
wide=1

window = Tk()
window.title("Exclusive Shop")
AI_Label = Label(text="AI Game Helper (Super OP) $29.99")
AI_Label.grid(row=1, column=0,columnspan=1)

def get_AI():
    global AI_enabed
    AI_purchase.config(text="Purchesed")
    AI_enabed=True

AI_purchase = Button(text="Buy",command=get_AI)
AI_purchase.grid(row=2, column=0,columnspan=1)

widen_lbl = Label(text="Widen Paddle ($9.98)")
widen_lbl.grid(row=1, column=1, columnspan=1)


def get_widen():
    global paddle,wide
    wide=4
    paddle.shapesize(stretch_wid=1, stretch_len=4)

widen_purchase = Button(text="Buy", command=get_widen)
widen_purchase.grid(row=2, column=1, columnspan=1)

important_note = Label(text="(NOTE: This is purely non-profit, all 'microtransactions' are just a touch of humor.")
important_note.grid(row=0, column=0,columnspan=2)

wants_faster_speed=True
wants_bal_speed=True
def buy_speedup():
    global bally
    set_paused(True)
    sign_in = Toplevel(window)
    sign_in.title("Would you like to buy 'faster speed'? ($3.99)")

    def yes_path():
        global speed
        speed+=7
        sign_in.destroy()
        set_paused(False)
        bally.x_speed*=15
        bally.y_speed*=15

    def no_path():
        global wants_faster_speed
        wants_faster_speed=False
        sign_in.destroy()
        set_paused(False)

    add_button2 = Button(sign_in,text="Yes", width=36, command=yes_path)
    add_button2.grid(row=1, column=1, columnspan=1)

    add_button = Button(sign_in, text="No", width=36,command=no_path)
    add_button.grid(row=1, column=0, columnspan=1)
    # This pauses until sign_in is closed, without freezing Turtle
    window.wait_window(sign_in)

def buy_moves():
    global bally
    moves=0
    set_paused(True)
    sign_in = Toplevel(window)
    sign_in.title("You ran out of paddle moves, would you like to buy more? (Cost below)")

    def yes_path():
        global paddle_moves
        global moves
        paddle_moves+=int(moves)
        print(paddle_moves)
        set_paused(False)
        sign_in.withdraw()

    def show_value(val):
        global moves
        label.config(text=f"Total Price: ${val}")
        moves=val
        return(val)

    slider = Scale(sign_in,from_=0, to=100, orient=HORIZONTAL, command=show_value)
    slider.grid(row=0, column=0, columnspan=1)
    label = Label(sign_in,text="Price: 0")
    label.grid(row=1, column=0, columnspan=1)
    add_button2 = Button(sign_in,text="Buy", width=36, command=yes_path)
    add_button2.grid(row=2, column=0, columnspan=1)
    # This pauses until sign_in is closed, without freezing Turtle
    window.wait_window(sign_in)

def buy_slowdown():
    global bally
    set_paused(True)
    sign_in = Toplevel(window)
    sign_in.title("Would you like to buy 'balanced speed'? ($13.99)")

    def yes_path():
        global speed
        speed-=4
        sign_in.destroy()
        set_paused(False)
        bally.x_speed*=(7/15)
        bally.y_speed*=(7/15)

    def no_path():
        global wants_bal_speed
        wants_bal_speed=False
        sign_in.destroy()
        set_paused(False)

    add_button2 = Button(sign_in,text="Yes", width=36, command=yes_path)
    add_button2.grid(row=1, column=1, columnspan=1)

    add_button = Button(sign_in, text="No", width=36,command=no_path)
    add_button.grid(row=1, column=0, columnspan=1)
    # This pauses until sign_in is closed, without freezing Turtle
    window.wait_window(sign_in)

def buy_respawn():
    global bally
    global revive_price

    set_paused(True)
    sign_in = Toplevel(window)
    if revive_price>1:
        sign_in.title("Would you like to buy 'respawn'? ($"+str(revive_price).split('.')[0]+".99)")
    else:
        sign_in.title("Would you like to buy 'respawn'? ($" + str(revive_price)[:4] + ")")

    def yes_path():
        global revive_price
        bally.respawn()
        revive_price *= 5.5
        revive_price=round(revive_price,2)
        sign_in.destroy()
        set_paused(False)

    def no_path():
        turtle.write("Game Over", align="center", font=("Courier", 50, "bold"))
        sign_in.destroy()

    add_button2 = Button(sign_in,text="Yes", width=36, command=yes_path)
    add_button2.grid(row=1, column=1, columnspan=1)

    add_button = Button(sign_in, text="No", width=36,command=no_path)
    add_button.grid(row=1, column=0, columnspan=1)
    # This pauses until sign_in is closed, without freezing Turtle
    window.wait_window(sign_in)

def buy_wall_bounce():
    global bally
    set_paused(True)
    sign_in = Toplevel(window)
    sign_in.title("Would you like to buy wall bounce ability ($0.99)")

    def yes_path():
        bally.CanWallBounce=True
        set_paused(False)
        sign_in.destroy()
        bally.wall_bounce()

    def no_path():
        sign_in.destroy()
        set_paused(False)
        bally.bal.teleport(bally.bal.xcor() + 30 * bally.x_speed, bally.bal.ycor() + 30 * bally.y_speed)

    add_button2 = Button(sign_in,text="Yes", width=36, command=yes_path)
    add_button2.grid(row=1, column=1, columnspan=1)

    add_button = Button(sign_in, text="No", width=36,command=no_path)
    add_button.grid(row=1, column=0, columnspan=1)
    # This pauses until sign_in is closed, without freezing Turtle
    window.wait_window(sign_in)

#Initiate breakout game using the library 'Turtle'
s = turtle.Screen()
setup(600, 1000)

rectCors = ((-10, 55), (10, 55), (10, -55), (-10, -55))
s.register_shape('rectangle2', ((-20, 55), (20, 55), (20, -55), (-20, -55)))
s.register_shape('rectangle', rectCors)

paddle = Turtle()
paddle.teleport(0, -350)
paddle.color("black")
paddle.pensize(5)
paddle.shape("rectangle")
paddle.penup()

class Brick:
    def __init__(self, color, x, y):
        self.t = Turtle()
        self.t.speed(0)
        self.t.shape("rectangle2")
        self.t.color(color)
        self.t.penup()
        self.t.teleport(x, y)
        self.x = x
        self.y = y
        self.width = 110
        self.height = 40

    def die(self):
        self.t.goto(999, 999)
        self.x = 999
        self.y = 999

    def ball_touching(self):
        global bally
        ball = bally.bal

        x_edge = False
        y_edge = False
        x2_edge = False
        y2_edge = False
        x_range = False
        y_range = False

        if (self.x - 10 - int(self.width / 2)) <= ball.xcor() <= (self.x + 10 - int(self.width / 2)):
            x_edge = True

        if (self.y - 10 - int(self.height / 2)) <= ball.ycor() <= (self.y + 10 - int(self.height / 2)):
            y_edge = True

        if (self.y - 10 + int(self.height / 2)) <= ball.ycor() <= (self.y + 10 + int(self.height / 2)):
            y2_edge = True

        if (self.x - 10 + int(self.width / 2)) <= ball.xcor() <= (self.x + 10 + int(self.width / 2)):
            x2_edge = True

        if (self.x - 10 - int(self.width / 2)) <= ball.xcor() <= (self.x + 10 + int(self.width / 2)):
            x_range = True

        if (self.y - 10 - int(self.height / 2)) <= ball.ycor() <= (self.y + 10 + int(self.height / 2)):
            y_range = True

        if x_edge and y_edge:
            self.die()
            return [-1, -1]
        elif x_edge and y2_edge:
            self.die()
            return [-1, 1]
        elif x2_edge and y2_edge:
            self.die()
            return [1, 1]
        elif x2_edge and y_edge:
            self.die()
            return [1, -1]
        elif x_edge and y_range:
            self.die()
            return [-1, 0]
        elif x2_edge and y_range:
            self.die()
            return [1, 0]
        elif x_range and y_edge:
            self.die()
            return [0, -1]
        elif x_range and y2_edge:
            self.die()
            return [0, 1]
        else:
            return [0, 0]

class bally:
    def __init__(self):
        self.bal = Turtle()
        self.bal.shape("circle")
        self.bal.color("black")
        self.bal.penup()
        self.x_speed = -speed
        self.y_speed = -speed
        self.CanWallBounce=False

    def wall_bounce(self):
        if self.bal.xcor() <= -290:
            if self.CanWallBounce:
                self.x_speed = speed
            else:
                buy_wall_bounce()
        if self.bal.xcor() >= 290:
            if self.CanWallBounce:
                self.x_speed = -speed
            else:
                buy_wall_bounce()

    def respawn(self):
        if self.bal.ycor() <= -500 or self.bal.xcor()>305 or self.bal.xcor()<-305:
            self.bal.teleport(0, 0)
            self.y_speed = -speed
            self.x_speed = random.choice([-speed, speed])

    def check_respawn(self):
        if self.bal.ycor() <= -500 or self.bal.xcor()>305 or self.bal.xcor()<-305:
            buy_respawn()
    def paddleB(self):
        global paddle,wide
        if (paddle.xcor() - 55*wide) <= self.bal.xcor() <= (paddle.xcor() + 55*wide) and \
           (paddle.ycor() - 20) <= self.bal.ycor() <= (paddle.ycor() + 20):
            self.y_speed = speed

    def go(self):
        self.bal.teleport(self.bal.xcor() + 1 * self.x_speed, self.bal.ycor() + 1 * self.y_speed)

    def topB(self):
        if self.bal.ycor() > 400:
            self.y_speed = -speed

    def brick_touch(self):
        global bricks
        for tst_brick3 in bricks:
            results = tst_brick3.ball_touching()
            if results[0] != 0:
                self.x_speed = results[0]*speed
            if results[1] != 0:
                self.y_speed = results[1]*speed

    def thing(self):
        self.go()
        self.wall_bounce()
        self.check_respawn()
        self.paddleB()
        self.topB()
        self.brick_touch()

bally = bally()

tst_brick = Brick("red", 70, 100)
tst_brick2 = Brick("red", -80, 100)
bricks = [tst_brick, tst_brick2, Brick("red", -230, 100), Brick("red", 220, 100),
          Brick("orange", -160, 160), Brick("orange", -10, 160), Brick("orange", 140, 160), Brick("orange", -310, 160), Brick("orange", 290, 160),
          Brick("yellow", -230, 220), Brick("yellow", 220, 220), Brick("yellow", 70, 220), Brick("yellow", -80, 220),
          Brick("limegreen", -160, 280), Brick("limegreen", -10, 280), Brick("limegreen", 140, 280), Brick("limegreen", -310, 280), Brick("limegreen", 290, 280),
          Brick("sky blue", -230, 340), Brick("sky blue", 220, 340), Brick("sky blue", 70, 340), Brick("sky blue", -80, 340),
          Brick("violet", -160, 400), Brick("violet", -10, 400), Brick("violet", 140, 400), Brick("violet", -310, 400), Brick("violet", 290, 400)]

# Pause system
paused = False

def set_paused(state):
    global paused
    paused = state
    print("Paused" if state else "Resumed")

# Paddle controls
def left():
    global paddle_moves
    if paddle_moves>=0:
        if paddle.xcor() >= -235:
            paddle.setx(paddle.xcor() - 20)
            paddle_moves-=1
    else:
        buy_moves()
def right():
    global paddle_moves
    if paddle_moves>=0:
        if paddle.xcor() <= 235:
            paddle.setx(paddle.xcor() + 20)
            paddle_moves-=1
    else:
        buy_moves()

# Debug controls
def debug1():
    bally.bal.setx(bally.bal.xcor() + 5)
    tst_brick.ball_touching()

def debug2():
    bally.bal.setx(bally.bal.xcor() - 5)
    tst_brick.ball_touching()

def debug3():
    bally.bal.sety(bally.bal.ycor() + 5)
    tst_brick.ball_touching()

def debug4():
    bally.bal.sety(bally.bal.ycor() - 5)

# Game loop with pause check
def game_loop():
    if not paused:
        bally.thing()
        if random.randint(1,200)==2:
            if speed==0.5 and wants_faster_speed:
                buy_speedup()
        if random.randint(1, 200) == 2:
            if speed==7.5 and wants_bal_speed:
                buy_slowdown()
    if AI_enabed:
        if paddle_moves >= 0:
            paddle.setx(bally.bal.xcor())
        else:
            buy_moves()


    turtle.ontimer(game_loop, 10)
# Key bindings
listen()
onkey(left, 'Left')
onkey(right, 'Right')
onkey(debug1, 'd')
onkey(debug2, 'a')
onkey(debug3, 'w')
onkey(debug4, 's')
# Start game
game_loop()
turtle.done()