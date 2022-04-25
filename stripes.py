
from pitop import Pitop
from PIL import ImageDraw

from pt_miniscreen.core import App
from pt_miniscreen.core import Component

miniscreen = Pitop().miniscreen  # miniscreen size 128, 64


class Stripes(Component):
    def render(self, image):
        image = image.convert("L")
        draw = ImageDraw.Draw(image)
        draw.rectangle(((0, 0), 12, 64), fill='#ffffff')
        draw.rectangle(((12, 0), 24, 64), fill='#e6e6e6')
        draw.rectangle(((24, 0), 36, 64), fill='#cccccc')
        draw.rectangle(((36, 0), 48, 64), fill='#b2b2b2')
        draw.rectangle(((48, 0), 60, 64), fill='#989898')
        draw.rectangle(((60, 0), 72, 64), fill='#7e7e7e')
        draw.rectangle(((72, 0), 84, 64), fill='#646464')
        draw.rectangle(((84, 0), 96, 64), fill='#4a4a4a')
        draw.rectangle(((96, 0), 108, 64), fill='#303030')
        draw.rectangle(((108, 0), 120, 64), fill='#161616')
        newimage = image.convert("1")
        # return the updated image
        return newimage



