from PIL import Image, ImageDraw
from pt_miniscreen.core import Component
from pt_miniscreen.core.components import Text
from pt_miniscreen.utils import get_font


class Counter(Component):

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
        self.create_interval(self.increment)

    def increment(self):
        # state lives in self.state
        self.state.update({"count": self.state["count"] + 1})

    def render(self, image):
        text = str(self.state["count"])

        ImageDraw.Draw(image).text(
            xy=(0, 0),
            text=text,
            font=get_font(12),
            fill="white"
        )

        padding = 10
        childImage = self.hello_world_text.render(image.crop(
            (padding, padding, image.height, image.width)))

        Image.Image.paste(image, childImage, (10, 10))

        # return the updated image
        return image
