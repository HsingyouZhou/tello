from ui.WubaGUI import Ui_MainWindow
from PySide2 import QtCore, QtGui, QtWidgets

from Single_Tello_Test.dr2 import movements as go
from Single_Tello_Test.dr2 import angles as degrees

# import PyPlot widget for our 3D plot
# from ..plot.plot import PlotWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    HORIZONTAL_MOVE = 30
    VERTICAL_MOVE = 30
    ROTATION_MOVE = 30


    def __init__(self):
        # This is equivalent to super(self.__class__, self).__init__()
        super().__init__()

        # Commands
        self.commands = {"go", "back", "forward", "cw", "ccw", "takeoff", "land"}

        self.setupUi(self)

        # Any changes to layout, etc. has to be done after UI setup
        # self.gRoot.addWidget(self.plot, 1, 1, 1, 1)
    
    # ------------------------
    # PROPERTIES
    # ------------------------

    @property
    def command_text(self):
        return self.lineEdit.text()

    @property
    def flying(self):
        return True

    @flying.setter
    def flying(self, flying):
        self.flying = flying

    # ------------------------
    # METHODS
    # ------------------------
    
    def append_command(self, command):
        self.teCommands.appendPlainText(command)

    # ------------------------
    # EVENT HANDLERS
    # ------------------------

    def on_turn_left(self):
        self.teCommands.appendPlainText(degrees("ccw", self.ROTATION_MOVE))

    def on_turn_right(self):
        self.teCommands.appendPlainText(degrees("cw", self.ROTATION_MOVE))

    def on_forward(self):
        self.teCommands.appendPlainText(go(self.HORIZONTAL_MOVE, 0, 0, self.leSpeed.text()))

    def on_back(self):
        self.teCommands.appendPlainText(go(-self.HORIZONTAL_MOVE, 0, 0, self.leSpeed.text()))

    def on_strafe_left(self):
        self.teCommands.appendPlainText(go(0, -self.HORIZONTAL_MOVE, 0, self.leSpeed.text()))

    def on_strafe_right(self):
        self.teCommands.appendPlainText(go(0, self.HORIZONTAL_MOVE, 0, self.leSpeed.text()))

    def on_down(self):
        self.teCommands.appendPlainText(go(0, 0, -self.VERTICAL_MOVE, self.leSpeed.text()))

    def on_up(self):
        # self.plot.fly_up()
        self.teCommands.appendPlainText(go(0, 0, self.VERTICAL_MOVE, self.leSpeed.text()))

    def on_add_command(self):
        command = self.command_text.split(" ")[0]
        if command in self.commands:
            self.append_command(self.command_text)
            return
        raise ValueError('Non-existing command!')

    def on_takeoff_land(self):
        print("on_takeoff_land")

    def on_pitch_up(self):
        print("on_pitch_up")

    def on_pitch_down(self):
        print("on_pitch_down")

    def on_pitch_reset(self):
        print("on_pitch_reset")

    def on_simulation(self):
        print("Simulatiooooon")

    def on_push_to_drone(self):
        print("pushing to drone... nothing")
