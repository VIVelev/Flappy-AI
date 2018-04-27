from turtle import *
from time import time, sleep
from random import randint
from subprocess import Popen
import sys
import glob

from .utils import *
from .bird import Bird

__all__ = [
    "Game",
]

class Game(object):
    def __init__(self, population, n_birds=10):
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

        self.best_txt = TextTurtle(90, 180, "white")
        self.tubes = [(GIFTurtle("./assets/img/tube1"), GIFTurtle("./assets/img/tube2")) for i in range(3)]
        self.grounds = [GIFTurtle("./assets/img/ground") for i in range(3)]

        self.n_birds = n_birds
        self.n_dead_birds = 0
        self.birds = population

        self.states = ["dead" for _ in range(n_birds)]
        self.scores = [0 for _ in range(n_birds)]
        self.best = 0

    def start_game(self):
        self.best = max(*self.scores, self.best)
        self.n_dead_birds = 0        
        self.tubes_y = [1000] * 3
        self.hit_t, self.hit_y = [0 for _ in range(self.n_birds)], [0 for _ in range(self.n_birds)]
        self.states = ["alive" for _ in range(self.n_birds)]
        self.tube_base = 0
        self.scores = [0 for _ in range(self.n_birds)]
        self.start_time = time()
        self.update_game()

    def compute_y(self, t, bird_i):
        return self.hit_y[bird_i] - 100 * (t - self.hit_t[bird_i]) * (t - self.hit_t[bird_i] - 1)

    def update_game(self):
        for i in range(self.n_birds):
            if self.states[i] == "dead":
                self.n_dead_birds += 1 
        
        if self.n_dead_birds == self.n_birds:
            sleep(1)
            self.fly(0)
            return

        for i in range(self.n_birds):
            vertical_dist = self.birds[i].body.ycor() - (self.tubes[-1][0].ycor() + self.tubes[-1][1].ycor())/2
            vertical_dist /= 1000
            horizontal_dist = self.tubes[-1][0].xcor()          
            if self.birds[i].should_fly([vertical_dist, horizontal_dist]) >= 0.5:
                self.fly(i)

        t = time() - self.start_time
        birds_y = [self.compute_y(t, i) for i in range(self.n_birds)]
        for i in range(self.n_birds):
            if birds_y[i] <= self.ground_line:
                birds_y[i] = self.ground_line
                self.states[i] = "dead"
                      
        x = int(t * self.speed_x)
        tube_base = -(x % self.tube_dist) - 40
        if self.tube_base < tube_base:
            if self.tubes_y[2] < 1000:
                for i in range(self.n_birds):
                    if self.states[i] == "alive":
                        self.scores[i] += 1

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

            lvecs = []
            rvecs = []
            for bird_y in birds_y:
                center = Vec2D(0, bird_y - 2)
                lvecs.append(Vec2D(tube_left, tube_upper) - center)
                rvecs.append(Vec2D(tube_right, tube_upper) - center)

            for i in range(self.n_birds):
                if (tube_left < 18 and tube_right > -18) and birds_y[i] - 12 <= tube_lower:
                    self.states[i] = "dead"
                if (tube_left <= 8 and tube_right >= -8) and birds_y[i] + 12 >= tube_upper:
                    self.states[i] = "dead"
                if abs(lvecs[i]) < 14 or abs(rvecs[i]) < 14:
                    self.states[i] = "dead"

        bg_base = -(x % self.bg_width)
        for i in range(3):
            self.grounds[i].goto(bg_base + self.bg_width * (i - 1), -200)

        for i in range(self.n_birds):
            self.birds[i].body.shape("./assets/img/bird%d.gif" % abs(int(t * 4) % 4 - 1))
            self.birds[i].body.goto(0, birds_y[i])

        if self.best:
            self.best_txt.clear()
            self.best_txt.write(
                "BEST: %d" % (self.best), align="center", font=(self.font_name, 14, "bold"))

        update()
        ontimer(lambda: self.update_game(), 10)

    def fly(self, bird_i):
        if "alive" not in self.states:
            self.start_game()
            return

        t = time() - self.start_time
        bird_y = self.compute_y(t, bird_i)
        if bird_y > self.ground_line:
            self.hit_t[bird_i], self.hit_y[bird_i] = t, bird_y

    def run(self):
        self.fly(0)
        mainloop()
