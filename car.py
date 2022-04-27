from random import random, randrange
import math
from PIL import ImageDraw
from pt_miniscreen.core import Component


class Wheel(Component):

    dx = 0
    dy = 0

    def __init__(self, **kwargs) -> None:
        # pass key word args to super
        super().__init__(**kwargs)
        # do setup

    # inside some kind of wheel component (of which there will be 2).
    # run on increment (frame)
    # responsible for controlling their general physics and collision
    def updateFrame(self):
        print("some stuff about the car's position")

    # def increment(self):
    #     # state lives in self.state
    #     # self.state.update({"count": self.state["count"] + 1})

    def render(self, image):
        # draw the outline of a rectangle on the passed image
        draw = ImageDraw.Draw(image)

        draw.polygon(self.level, fill="white")

        # return the updated image
        return image
