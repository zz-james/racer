from PIL import Image, ImageDraw
from pt_miniscreen.core import Component
from pt_miniscreen.core.components import Text
from pt_miniscreen.utils import get_font


class Experiment(Component):

    default_state = {"count": 0}

    def __init__(self, **kwargs) -> None:
        # pass key word args to super
        # you can update the parents initial state here if you want by passing initial_state={"blah":blah} in the super __init__ params
        super().__init__(**kwargs)
        # do setup e.g. create child components
        # to create a child, pass a component's class as the first argument of 'create_child'
        # Add any arguments you need to pass to the component as additional arguments.
        # Store the child in an attribute, in this case 'hello_world_text' is used
        self.hello_world_text = self.create_child(Text, text="Hello World!")

        # pass the method you want called to `create_interval`. By default it runs
        # the method every second.
        # self.create_interval(self.increment)

    # def increment(self):
    #     # state lives in self.state
    #     self.state.update({"count": self.state["count"] + 1})
    # def dashedLine(self, draw, x, y, dx, dy):
    #    draw.line((x, y, x+dx, y+dy), fill="white")
    def drawCircle(self, draw, radius, x=64, y=32):
        circle = [x - (radius/2), y - (radius/2), x + radius/2, y+radius/2]
        draw.ellipse(circle, outline='white')

    def drawStar(self, draw, x=64, y=32, scale=1):
        points = [
            x, y,
            x + 20 * scale, y - 40 * scale,
            x + 30 * scale, y + 10 * scale,
            x, y-30 * scale,
            x + 40 * scale, y - 20 * scale
        ]

        draw.polygon(points,  fill="white")

    def render(self, image):

        draw = ImageDraw.Draw(image)

        x_anchor = 15
        y_anchor = 32
        self.drawStar(draw, x_anchor, y_anchor)

        x_anchor = 50
        y_anchor = 50
        self.drawStar(draw, x_anchor, y_anchor, 1.2)

        x_anchor = 90
        y_anchor = 70
        self.drawStar(draw, x_anchor, y_anchor, 1.5)

        # return the updated image
        return image
