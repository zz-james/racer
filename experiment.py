from PIL import Image, ImageDraw
import random
import math
from pt_miniscreen.core import Component
from pt_miniscreen.core.components import Text
from pt_miniscreen.utils import get_font


class Experiment(Component):

    # ball_radius = 15
    # default_state = {"pos_x": 1, "pos_y": 1}
    # shift_x = 10
    # shift_y = 5
    carImage = Image.open('car.tif')

    def __init__(self, **kwargs) -> None:
        # pass key word args to super
        # you can update the parents initial state here if you want by passing initial_state={"blah":blah} in the super __init__ params
        super().__init__(**kwargs)

        basey = 64  # bottom of screen
        x = 0  # where are we along
        ang = 0  # gradient of hill
        hei = basey - 56  # max height for terrain
        pit = 0  # how many pits have we made
        lastpit = 0  # used to make sure pits aren't too close together
        boulderCount = 0  # number of boulders we made

        ground.clear()
        ground.moveTo(0, basey)  # move to the bottom left
        # fill method of the draw api - anything we draw from now on is a solid shape (polygon?)
        ground.beginFill(0x915039)

        ground.instanceEmptyMovieClip("objs", 1)  # ?

        steps = 0

        # this is the start of a large loop within makeRandomTerrain which is responsible for creating the physical terrain
        # our levels are a maximum width of 15100 px. the level is created through a series of segments each attached to the next
        # a segment can be between 100 and 50 px wide. each segment can be at any angle.

        # once we have calculate this width and stored it in wid, we then modify the hei variable based on that width, multiplied
        # by the sin value of the angle.

        # after the segment has been created we modify the angle variable by increasing or decreasing it by up to -1 or 1 this means
        # anything between 0 and 1 will increase the angle (slope down) and anything between 0 and -1 will decrease the angle (slope up)
        while x < 15100:
            wid = random.random() * 100 + 50
            hei += math.sin(ang) * wid
            ang += (random.random() * 2) - 1

        # responsible for controlling the vertical endpoint of the current segment.
        # if pit > 0 that means we're drawing a pit so height is off the bottom of the screen
        # then decrement the pit variable - we set the pit variable to between 2 and 5 which determines how wide it will be
        # otherwise in the second if statement, if the hei value has somehow reached - 100 then we set it back to -100 and change the
        # angle to 0.1. when the hei variable is less than 100 (heading off the top of the screen) so we force it to halt its ascent
        # and change it ang to -0.1 which will make it angle down slightly. this has the effectt of making bumpy platues
        # the third if statement checks to see if the hull has reached the ground level following the same rules.
            if pit > 0:
                hei = basey + 150
                pit -= 1
            elif hei < -100:
                hei = -100
                ang = 0.1
            elif hei > basey - 100:
                hei = basey - 100
                ang = -0.1

        # do setup e.g. create child components
        # to create a child, pass a component's class as the first argument of 'create_child'
        # Add any arguments you need to pass to the component as additional arguments.
        # Store the child in an attribute, in this case 'hello_world_text' is used
        # self.hello_world_text = self.create_child(Text, text="Hello World!")

        # pass the method you want called to `create_interval`. By default it runs
        # the method every second.
        # self.create_interval(self.increment, 0.1)

    # def increment(self):
    #     # state lives in self.state
    #     self.state.update(
    #         {"pos_x": self.state["pos_x"] + self.shift_x, "pos_y": self.state["pos_y"] + self.shift_y})

    # def drawCircle(self, draw, radius, x=64, y=32):
    #     circle = [x - (radius/2), y - (radius/2), x + radius/2, y+radius/2]
    #     draw.ellipse(circle, outline='white')

    def render(self, image):

        # draw = ImageDraw.Draw(image)

        # points = [self.state['pos_x'], self.state['pos_y'],
        #           self.state['pos_x'] + self.ball_radius, self.state['pos_y'] + self.ball_radius]
        Image.Image.paste(image, self.carImage, (10, 10))
        # draw.ellipse(points, fill="white")

        # return the updated image
        return image
