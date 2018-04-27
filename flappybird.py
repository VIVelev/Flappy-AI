from turtle import *
from time import time, sleep
from random import randint
from subprocess import Popen
import sys
import glob

__all__ = [
    "Game",
]

class Game(object):
    def __init__(self):
        screensize(216, 500)
        bgpic("./assets/img/bg1.gif")        
        setup(288, 512)
        tracer(False, 0)
        hideturtle()
        for f in glob.glob("./assets/img/*.gif"):
            addshape(f)

        self.font_name = "Comic Sans MS"
        self.speed_x = 100
        self.ground_line = -200 + 56 + 12
        self.tube_dist = 230
        self.bg_width = 286

        self.score_txt = self.TextTurtle(0, 130, "white")
        self.best_txt = self.TextTurtle(90, 180, "white")
        self.tubes = [(self.GIFTurtle("./assets/img/tube1"), self.GIFTurtle("./assets/img/tube2")) for i in range(3)]
        self.grounds = [self.GIFTurtle("./assets/img/ground") for i in range(3)]
        self.birds = [self.GIFTurtle("./assets/img/bird1")]

        self.state = "end"
        self.score = self.best = 0

    def TextTurtle(self, x, y, color):
        t = Turtle()
        t.hideturtle()
        t.up()
        t.goto(x, y)
        t.speed(0)
        t.color(color)
        return t

    def GIFTurtle(self, fname):
        t = Turtle(fname + ".gif")
        t.speed(0)
        t.up()
        return t

    def start_game(self):
        self.best = max(self.score, self.best)
        self.tubes_y = [10000] * 3
        self.hit_t, self.hit_y = 0, 0
        self.state = "alive"
        self.tube_base = 0
        self.score = 0
        self.start_time = time()
        self.update_game()

    def compute_y(self, t):
        return self.hit_y - 100 * (t - self.hit_t) * (t - self.hit_t - 1)

    def update_game(self):
        if self.state == "dead":
            sleep(1)
            self.state = "end"
            return

        t = time() - self.start_time
        bird_y = self.compute_y(t)

        if bird_y <= self.ground_line:
            bird_y = self.ground_line
            self.state = "dead"

        x = int(t * self.speed_x)
        tube_base = -(x % self.tube_dist) - 40
        if self.tube_base < tube_base:
            if self.tubes_y[2] < 1000:
                self.score += 1
            self.tubes_y = self.tubes_y[1:] + [randint(-100, 50)]
        self.tube_base = tube_base

        for i in range(3):
            self.tubes[i][0].goto(
                tube_base + self.tube_dist * (i - 1), 250 + self.tubes_y[i])
            self.tubes[i][1].goto(
                tube_base + self.tube_dist * (i - 1), -150 + self.tubes_y[i])

        if self.tubes_y[2] < 1000:
            tube_left = tube_base + self.tube_dist - 28
            tube_right = tube_base + self.tube_dist + 28
            tube_upper = self.tubes_y[2] + 250 - 160
            tube_lower = self.tubes_y[2] - 150 + 160
            center = Vec2D(0, bird_y - 2)
            lvec = Vec2D(tube_left, tube_upper) - center
            rvec = Vec2D(tube_right, tube_upper) - center
            if (tube_left < 18 and tube_right > -18) and bird_y - 12 <= tube_lower:
                self.state = "dead"
            if (tube_left <= 8 and tube_right >= -8) and bird_y + 12 >= tube_upper:
                self.state = "dead"
            if abs(lvec) < 14 or abs(rvec) < 14:
                self.state = "dead"

        bg_base = -(x % self.bg_width)
        for i in range(3):
            self.grounds[i].goto(bg_base + self.bg_width * (i - 1), -200)
        
        for bird in self.birds:
            bird.shape("./assets/img/bird%d.gif" % abs(int(t * 4) % 4 - 1))
            bird.goto(0, bird_y)

        self.score_txt.clear()
        self.score_txt.write("%s" % (self.score), align="center", font=(self.font_name, 80, "bold"))

        if self.best:
            self.best_txt.clear()
            self.best_txt.write(
                "BEST: %d" % (self.best), align="center", font=(self.font_name, 14, "bold"))

        update()
        ontimer(lambda: self.update_game(), 10)

    def fly(self):
        if self.state == "end":
            self.start_game()
            return
        t = time() - self.start_time
        bird_y = self.compute_y(t)
        if bird_y > self.ground_line:
            self.hit_t, self.hit_y = t, bird_y

    def main(self):
        onkey(self.fly, "space")
        listen()
        mainloop()
        sys.exit(1)

if __name__ == "__main__":
    game = Game()
    game.main()
