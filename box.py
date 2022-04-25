from PIL import ImageDraw
from pt_miniscreen.core import Component


class Box(Component):

    default_state = {"count": 0}

    def __init__(self, **kwargs) -> None:
        # pass key word args to super
        super().__init__(**kwargs)
        # do setup

    def speak(self):
        print(self.state["count"])

    def increment(self):
        # state lives in self.state
        self.state.update({"count": self.state["count"] + 1})

    def render(self, image):
        # draw the outline of a rectangle on the passed image
        draw = ImageDraw.Draw(image)
        draw.rectangle(
            ((10, 10), image.size[0] - 10, image.size[1] - 10), outline="white")

        # return the updated image
        return image
