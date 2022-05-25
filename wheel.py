import os
from random import random, randrange
import math
from PIL import ImageDraw
from pt_miniscreen.core import Component


class Wheel(Component):

    dx = 0
    dy = 0   # vertical speed
    x = 0
    y = 0
    accelerating = False

    def __init__(self, inGround=None, **kwargs):
        # pass key word args to super
        super().__init__(**kwargs)
        self.inGround = inGround
        # if no groud then throw or something

    # inside some kind of wheel component (of which there will be 2).
    # run on increment (frame)
    # responsible for controlling their general physics and collision
    def wheelControl(self, LEFT_PRESSED, RIGHT_PRESSED):
        # immediately we apply vertical motion to the wheel
        # this could be negative (up) or positive (down)
        # the value of dy is set by a number of things
        # accelerating is a boolean determined by keypress
        self.y += self.dy

        accelerating = False
        onGround = True  # make this false

        if RIGHT_PRESSED and onGround:
            self.dx += 0.3
            mydir = 1
            accelerating = True

        if LEFT_PRESSED and onGround:
            self.dx -= 0.3
            mydir = -1
            accelerating = True

        # above: this code is responsible for accepting user input. first we check to see if the player is pressing the right button
        # if so, and at least one wheel is on the ground we increase the wheel's dx by 0.3, set the valie of the mydir variables to 1
        # and set the value of the accelerating variable too.
        # By increasing dx, rather than simply moving _x, we create a motion by which the vehicle gradually speeds up from a motionless state
        # and vice-versa for the left key
        # if accelerating and (abs(self.dx) < 0.5):
            # make engine sound
            # os.system('aplay squeal.wav')

        # # apply natural forces to the wheel. The first line applies some friction (slowing)
        # # the second line is gravity (on mars)
        if onGround:
            self.dx *= 0.98

        self.dy += 0.5

        # controlling arbitraty collision with the ground
        # if self.inGround(self.x, self.y):
        #     # first make sure that the wheel is touching the terrain
        #     # figure out how deep it is
        #     # if ground slopes up we ned to make sure that the wheel is moved up to the first valid position that is not in the ground
        #     # tricky because of slopes
        #     ty = self.y
        #     cnt = 0
        #     while self.ground.hitTest(self.x, ty):
        #         ty -= 1
        #         cnt += 1
        #     # when the loop ends we will be left with a y value in ty which is the place to put the wheel. we also increment cnt because we need it

        #     # cnt is the numberof pixels the climb consists of. One average, when we're going up small slopes cnt < 5
        #     # the purpose of cnt is to determine if we have a really high climb. this happens if we hit a wall

        #     if cnt > 70:
        #         # hit a wall - we reverse the direction of both wheels

        #         self.dx *= -1
        #         # wheel1.dx *= -1
        #         self.ground.x -= self.dx
        #         # play crash sound
        #     else:
        #         self.y = ty
        #         if cnt < 5:
        #             cnt = 0
        #             self.y += -cnt / 3  # gives the wheel some vertical velocity due to the hill it climbed
        #             self.onGround = True  # should this be oneOnGround?
        # else:
        #     self.onGround = False

        # apply caps to the maximum vertical speed a wheel can have
        if self.dy > 15:
            self.dy = 15

        if self.dy < -15:
            self.dy = -15

        print(self.y)

        self.state.update(
            {'dy': self.dy, 'dx': self.dx}
        )

    # def increment(self):
    #     # state lives in self.state
    #     # self.state.update({"count": self.state["count"] + 1})

    def render(self, image):
        # draw the outline of a rectangle on the passed image
        # draw = ImageDraw.Draw(image)
        print('wheel render')
        # return the updated image
        return image
