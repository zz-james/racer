# composes a frame

from PIL import ImageDraw
from pt_miniscreen.core import Component
import ground
import wheel


class Frame(Component):

    RIGHT_PRESSED = False
    LEFT_PRESSED = False

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ground = self.create_child(ground.Ground)
        self.wheel0 = self.create_child(wheel.Wheel, ground=self.ground)

        # self.wheel1 = self.create_child(wheel.Wheel)

        self.create_interval(self.make_frame, 1 / 24)

    def make_frame(self):
        self.ground.updateFrame(self.wheel0)
        self.wheel0.wheelControl(self.LEFT_PRESSED, self.RIGHT_PRESSED)

    def render(self, image):
        return self.ground.render(image.crop(
            (0, 0, image.height, image.width)
        ))