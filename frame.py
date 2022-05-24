# composes a frame

from PIL import ImageDraw, Image
from pt_miniscreen.core import Component
import ground


# this is the root component


class Frame(Component):

    RIGHT_PRESSED = False
    LEFT_PRESSED = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ground = self.create_child(ground.Ground)
        self.create_interval(self.make_frame, 1 / 24)

    def make_frame(self):
        # self.wheely.wheelControl(self.LEFT_PRESSED, self.RIGHT_PRESSED)
        self.ground.updateFrame(self.LEFT_PRESSED, self.RIGHT_PRESSED)

    def render(self, image):  # my root component recieves an image from the miniscreen app
        return self.ground.render(image.crop(
            (0, 0, image.height, image.width)
        ))
