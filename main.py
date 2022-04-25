import signal
from pitop import Pitop
import experimentApp


miniscreen = Pitop().miniscreen  # miniscreen size 128, 64

eApp = experimentApp.ExperimentApp(miniscreen)
eApp.start()
signal.pause()
