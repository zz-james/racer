from PIL import Image, ImageDraw
from pt_miniscreen.core import Component
from pt_miniscreen.core.components import Text
from pt_miniscreen.utils import get_font


class Experiment(Component):

    ball_radius = 15
    default_state = {"pos_x": 1, "pos_y": 1}
    shift_x = 10
    shift_y = 5

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
        self.create_interval(self.increment, 0.1)

    def increment(self):
        # state lives in self.state
        self.state.update(
            {"pos_x": self.state["pos_x"] + self.shift_x, "pos_y": self.state["pos_y"] + self.shift_y})

    def drawCircle(self, draw, radius, x=64, y=32):
        circle = [x - (radius/2), y - (radius/2), x + radius/2, y+radius/2]
        draw.ellipse(circle, outline='white')

    def render(self, image):

        draw = ImageDraw.Draw(image)

        points = [self.state['pos_x'], self.state['pos_y'],
                  self.state['pos_x'] + self.ball_radius, self.state['pos_y'] + self.ball_radius]

        draw.ellipse(points, fill="white")

        # return the updated image
        return image
