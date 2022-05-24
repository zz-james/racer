from random import random, randrange
import math
from PIL import ImageDraw, Image
from pt_miniscreen.core import Component
import wheel


class Ground(Component):
    lives = 4  # move this
    level = []
    x = 0
    y = 295
    levelSize = 15100

    def __init__(self, **kwargs):
        # pass key word args to super
        super().__init__(**kwargs)
        # do setup
        self.wheely = self.create_child(wheel.Wheel)

        # make the source image
        self.ground = self.makeRandomTerrain(
            Image.new('RGB', (self.levelSize, 128), (0, 0, 0)))  # need to make this the right width and height

    def makeRandomTerrain(self, pImage):
        baseY = 120  # bottom of screen
        x = 0  # where are we along
        angle = 0  # gradient of hill
        height = 10  # the height of the terrain is 128 - height
        pit = 0  # how many pits have we made
        lastpit = 0  # used to make sure pits aren't too close together
        boulderCount = 0  # number of boulders we made
        line = []

        # clear any existing ground
        # move to bottom left of shape
        line.extend([x, baseY])
        # set fill colour

        steps = 0

        # this is the start of a large loop within makeRandomTerrain which is responsible for creating the physical terrain
        # our levels are a maximum width of 15100 px. the level is created through a series of segments each attached to the next
        # a segment can be between 100 and 50 px wide. each segment can be at any angle.

        # once we have calculate this width and stored it in segWidth, we then modify the height variable based on that width, multiplied
        # by the sin value of the angle.

        # after the segment has been created we modify the angle variable by increasing or decreasing it by up to -1 or 1 this means
        # anything between 0 and 1 will increase the angle (slope down) and anything between 0 and -1 will decrease the angle (slope up)
        while x < self.levelSize:
            segWidth = random() * 100 + 50
            height += math.sin(angle) * segWidth
            oldHeight = height  # ?
            angle += (random() * 0.5) - 0.25

            # responsible for controlling the vertical endpoint of the current segment.
            # if pit > 0 that means we're drawing a pit so height is off the bottom of the screen
            # then decrement the pit variable - we set the pit variable to between 2 and 5 which determines how wide it will be
            # otherwise in the second if statement, if the height value has somehow reached - 100 then we set it back to -100 and change the
            # angle to 0.1. when the height variable is less than 100 (heading off the top of the screen) so we force it to halt its ascent
            # and change it angle to -0.1 which will make it angle down slightly. this has the effectt of making bumpy platues
            # the third if statement checks to see if the hull has reached the ground level following the same rules.
            if pit > 0:
                height = baseY + 32  # height goes off the bottom
                pit -= 1
            elif height < 20:  # it went up too far
                height = 20
                angle = +0.1
            elif height > baseY:  # it went down too far
                height = baseY - 10
                angle = -0.1

            # generation of pits and canyons
            if lastpit > 0:
                lastpit -= 1

            if random() < 0.033 and pit == 0 and x > 700 and lastpit == 0:
                # begin pit
                pit = math.floor(random() * 3) + 3
                lastpit = pit + 5
                # make this 10 px higher than the height at the end of the last itteration
                height = oldHeight + 20

            x += segWidth

            if randrange(10) > 5:
                # draw lineTo(x, height)
                line.extend([x, height])
            else:
                # curveTo(line[-2], line[-1], x+segWidth, height): no curve api :-(
                line.extend([x, height])

                # make a boulder
                # if random() < 0.1 and angle > -0.1 and x > 500 and x < 14000:

                # make a water droplet
                # if((steps % 25) == 20)

            steps += 1
            oldHeight = height  # store the old height so we can use it in the next itteration

        # do finish line
        line.extend([x, baseY + 100])
        line.extend([0, baseY + 100])

        draw = ImageDraw.Draw(pImage)
        draw.polygon(line, fill=(255, 0, 0))
        pImage.show()
        return pImage

    # determine is the x and y is inside the ground
    # we can probably grab a pixel, if it is white it is in the ground
    def hitTest(self, x, y):
        return self.ground.getPixel(x, y)

    # def increment(self):
    #     # state lives in self.state
    #     # self.state.update({"count": self.state["count"] + 1})

    def updateFrame(self, LEFT_PRESSED, RIGHT_PRESSED):
        # this._x -= wheel1.dx;
        self.wheely.wheelControl(LEFT_PRESSED, RIGHT_PRESSED)

        self.x += self.wheely.dx

        # print(self.x)
        # print('--------------')
        # the vehicle doesn't move, the ground movie clip moves backwards
        # so starting at 0 it becomes negative
        # the wheels only move up and down
        if self.x < 0:
            self.x = 0
            self.wheely.dx = 0
            # this stops all wheel motion and moves the ground to 0 if the value of ground > 1
            # stops the player driving off the left

        # if you fall into a pit
        # if wheel.y > 600:
        #     print('wheel y is greater than 600')
        #     if self.lives == 0:
        #         # set fail state
        #         # stop everything

        #         # fall to death in a pit
        #         wheel.y = 100
        #         wheel.dx = 0
        #         wheel.dy = 0
        #         self.x = 0
        #         self.lives -= 1

        # finish
        if self.x > 15000:
            self.wheely.y = 100
            self.wheely.dx = 0
            self.x = 0
        # some kind of result.

        print('--')
        print(self.x)

    def render(self, image):

        # paste ground onto image
        onebit = self.ground.convert("1")
        # onebit.show()
        # return the updated image
        return onebit.crop((0 + self.x, 0, image.height + self.x, image.width))
