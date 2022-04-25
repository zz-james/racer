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

    def render(self, image):
        # text = str(self.state["count"])

        # ImageDraw.Draw(image).text(
        #     xy=(0, 0),
        #     text=text,
        #     font=get_font(12),
        #     fill="white"
        # )

        # kinky_line = [10, 10, 50, 45, 128, 64]

        draw = ImageDraw.Draw(image)
        # draw.line(kinky_line, fill="white", joint="curve")

        centre_x = 64
        centre_y = 32
        radius = 60
        number_of_rings = 15

        for i in range(0, number_of_rings):
            self.drawCircle(draw, radius)
            radius -= 4

        # circle = [centre_x - (radius/2), centre_y - (radius/2), centre_x + radius/2, centre_y+radius/2]
        # draw.ellipse(circle, fill = 'blue', outline ='blue')

        # circle = [centre_x - (radius/2), centre_y - (radius/2), centre_x + radius/2, centre_y+radius/2]

        # draw.ellipse(circle, fill = 'blue', outline ='blue')
        # self.dashedLine(draw, 10, 10, 50, 100)
        # padding = 10
        # childImage = self.hello_world_text.render(image.crop(
        #     (padding, padding, image.height, image.width)))

        # Image.Image.paste(image, childImage, (10, 10))

        # return the updated image
        return image
