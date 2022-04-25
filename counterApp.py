from pt_miniscreen.core import App
import counter


class CounterApp(App):
    def __init__(self, miniscreen):
        super().__init__(miniscreen, Root=counter.Counter)

        miniscreen.select_button.when_released = self.onSelectRelease

    def onSelectRelease(self):
        self.root.increment()
