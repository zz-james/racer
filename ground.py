from random import random, randrange
import math
from PIL import ImageDraw
from pt_miniscreen.core import Component


class Ground(Component):

    level = []

    def __init__(self, **kwargs) -> None:
        # pass key word args to super
        super().__init__(**kwargs)
        # do setup
        self.level = self.makeRandomTerrain()

    def makeRandomTerrain(self):
        basey = 250  # bottom of screen
        x = 0  # where are we along
        ang = 0  # gradient of hill
        hei = basey - 220  # max height for terrain
        pit = 0  # how many pits have we made
        lastpit = 0  # used to make sure pits aren't too close together
        boulderCount = 0  # number of boulders we made
        line = []

        # clear any existing ground
        # move to bottom left of shape
        line.extend([x, basey])
        # set fill colour

        steps = 0

        # this is the start of a large loop within makeRandomTerrain which is responsible for creating the physical terrain
        # our levels are a maximum width of 15100 px. the level is created through a series of segments each attached to the next
        # a segment can be between 100 and 50 px wide. each segment can be at any angle.

        # once we have calculate this width and stored it in wid, we then modify the hei variable based on that width, multiplied
        # by the sin value of the angle.

        # after the segment has been created we modify the angle variable by increasing or decreasing it by up to -1 or 1 this means
        # anything between 0 and 1 will increase the angle (slope down) and anything between 0 and -1 will decrease the angle (slope up)
        while x < 15100:
            wid = random() * 100 + 50
            hei += math.sin(ang) * wid
            ohei = hei
            ang += (random() * 2) - 1

            # responsible for controlling the vertical endpoint of the current segment.
            # if pit > 0 that means we're drawing a pit so height is off the bottom of the screen
            # then decrement the pit variable - we set the pit variable to between 2 and 5 which determines how wide it will be
            # otherwise in the second if statement, if the hei value has somehow reached - 100 then we set it back to -100 and change the
            # angle to 0.1. when the hei variable is less than 100 (heading off the top of the screen) so we force it to halt its ascent
            # and change it ang to -0.1 which will make it angle down slightly. this has the effectt of making bumpy platues
            # the third if statement checks to see if the hull has reached the ground level following the same rules.
            if pit > 0:
                hei = basey + 400
                pit -= 1
            elif hei < -100:
                hei = -100
                ang = 0.1
            elif hei > basey - 100:
                hei = basey - 100
                ang = -0.1

            # generation of pits and canyons
            if lastpit > 0:
                lastpit -= 1

            if random() < 0.033 and pit == 0 and x > 700 and lastpit == 0:
                # begin pit
                pit = math.floor(random() * 3) + 3
                lastpit = pit + 5
                hei = ohei - 40  # wtf

            x += wid

            if randrange(10) > 5:
                # draw lineTo(x, hei)
                line.extend([x, hei])
            else:
                # bob = curveTo(line[-2], line[-1], x+wid, hei)
                line.extend([x, hei])

                # make a boulder
                # if random() < 0.1 and ang > -0.1 and x > 500 and x < 14000:

                # make a water droplet
                # if((steps % 25) == 20)

            steps += 1
            ohei = hei

        # do finish line
        line.extend([x, basey + 400])
        line.extend([0, basey+400])
        return line

    # def increment(self):
    #     # state lives in self.state
    #     # self.state.update({"count": self.state["count"] + 1})

    def render(self, image):
        # draw the outline of a rectangle on the passed image
        draw = ImageDraw.Draw(image)

        draw.polygon(self.level, fill="white")

        # return the updated image
        return image
