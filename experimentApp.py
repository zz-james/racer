from pt_miniscreen.core import App
import frame


class ExperimentApp(App):
    def __init__(self, miniscreen):  # miniscreen size 128, 64
        super().__init__(miniscreen, Root=frame.Frame)
        # self.miniscreen.up_button.when_pressed = self.handle_up_pressed
        # self.miniscreen.up_button.when_released = self.handle_up_released
        # self.miniscreen.down_button.when_pressed = self.handle_down_pressed
        # self.miniscreen.down_button.when_released = self.handle_down_released
        self.miniscreen.select_button.when_pressed = self.handle_select_pressed
        self.miniscreen.select_button.when_released = self.handle_select_released
        self.miniscreen.cancel_button.when_pressed = self.handle_cancel_pressed
        self.miniscreen.cancel_button.when_released = self.handle_cancel_released

    # def handle_up_pressed(self):
    #     self.root.start_rotating_ship_clockwise()

    # def handle_down_pressed(self):
    #     self.root.start_rotating_ship_anticlockwise()

    # def handle_up_released(self):
    #     self.root.stop_rotating_ship_clockwise()

    # def handle_down_released(self):
    #     self.root.stop_rotating_ship_anticlockwise()

    def handle_select_pressed(self):
        self.root.RIGHT_PRESSED = True

    def handle_select_released(self):
        self.root.RIGHT_PRESSED = False

    def handle_cancel_pressed(self):
        self.root.LEFT_PRESSED = True

    def handle_cancel_released(self):
        self.root.LEFT_PRESSED = False
