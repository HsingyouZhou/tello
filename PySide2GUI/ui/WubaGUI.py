# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PySide2GUI/ui/WubaGUI.ui',
# licensing of 'PySide2GUI/ui/WubaGUI.ui' applies.
#
# Created: Sat Nov  9 14:20:18 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 799, 719))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gRoot = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gRoot.setContentsMargins(-1, -1, -1, 21)
        self.gRoot.setObjectName("gRoot")
        self.gButtons = QtWidgets.QGridLayout()
        self.gButtons.setContentsMargins(0, 0, 0, 0)
        self.gButtons.setObjectName("gButtons")
        self.bTurnLeft_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bTurnLeft_2.sizePolicy().hasHeightForWidth())
        self.bTurnLeft_2.setSizePolicy(sizePolicy)
        self.bTurnLeft_2.setAutoRepeatDelay(100)
        self.bTurnLeft_2.setObjectName("bTurnLeft_2")
        self.gButtons.addWidget(self.bTurnLeft_2, 0, 0, 1, 1)
        self.bUp_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bUp_2.sizePolicy().hasHeightForWidth())
        self.bUp_2.setSizePolicy(sizePolicy)
        self.bUp_2.setAutoRepeatDelay(100)
        self.bUp_2.setObjectName("bUp_2")
        self.gButtons.addWidget(self.bUp_2, 2, 2, 1, 1)
        self.bTurnRight_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bTurnRight_2.sizePolicy().hasHeightForWidth())
        self.bTurnRight_2.setSizePolicy(sizePolicy)
        self.bTurnRight_2.setAutoRepeatDelay(100)
        self.bTurnRight_2.setObjectName("bTurnRight_2")
        self.gButtons.addWidget(self.bTurnRight_2, 0, 2, 1, 1)
        self.bForward_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bForward_2.sizePolicy().hasHeightForWidth())
        self.bForward_2.setSizePolicy(sizePolicy)
        self.bForward_2.setAutoRepeatDelay(100)
        self.bForward_2.setObjectName("bForward_2")
        self.gButtons.addWidget(self.bForward_2, 0, 1, 1, 1)
        self.bStrafeRight_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bStrafeRight_2.sizePolicy().hasHeightForWidth())
        self.bStrafeRight_2.setSizePolicy(sizePolicy)
        self.bStrafeRight_2.setAutoRepeatDelay(100)
        self.bStrafeRight_2.setObjectName("bStrafeRight_2")
        self.gButtons.addWidget(self.bStrafeRight_2, 1, 2, 1, 1)
        self.bShtrafeLeft_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bShtrafeLeft_2.sizePolicy().hasHeightForWidth())
        self.bShtrafeLeft_2.setSizePolicy(sizePolicy)
        self.bShtrafeLeft_2.setAutoRepeatDelay(100)
        self.bShtrafeLeft_2.setObjectName("bShtrafeLeft_2")
        self.gButtons.addWidget(self.bShtrafeLeft_2, 1, 0, 1, 1)
        self.bTakeOffLand_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bTakeOffLand_2.sizePolicy().hasHeightForWidth())
        self.bTakeOffLand_2.setSizePolicy(sizePolicy)
        self.bTakeOffLand_2.setAutoRepeatDelay(100)
        self.bTakeOffLand_2.setObjectName("bTakeOffLand_2")
        self.gButtons.addWidget(self.bTakeOffLand_2, 1, 1, 1, 1)
        self.bBack_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bBack_2.sizePolicy().hasHeightForWidth())
        self.bBack_2.setSizePolicy(sizePolicy)
        self.bBack_2.setAutoRepeatDelay(100)
        self.bBack_2.setObjectName("bBack_2")
        self.gButtons.addWidget(self.bBack_2, 2, 1, 1, 1)
        self.bDown_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bDown_2.sizePolicy().hasHeightForWidth())
        self.bDown_2.setSizePolicy(sizePolicy)
        self.bDown_2.setAutoRepeatDelay(100)
        self.bDown_2.setObjectName("bDown_2")
        self.gButtons.addWidget(self.bDown_2, 2, 0, 1, 1)
        self.gRoot.addLayout(self.gButtons, 1, 0, 1, 1)
        self.hCommands = QtWidgets.QHBoxLayout()
        self.hCommands.setObjectName("hCommands")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.hCommands.addWidget(self.lineEdit)
        self.bAddCommand = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bAddCommand.sizePolicy().hasHeightForWidth())
        self.bAddCommand.setSizePolicy(sizePolicy)
        self.bAddCommand.setObjectName("bAddCommand")
        self.hCommands.addWidget(self.bAddCommand)
        self.gRoot.addLayout(self.hCommands, 2, 0, 1, 1)
        self.teCommands = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teCommands.sizePolicy().hasHeightForWidth())
        self.teCommands.setSizePolicy(sizePolicy)
        self.teCommands.setObjectName("teCommands")
        self.gRoot.addWidget(self.teCommands, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.sbStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.sbStatusBar.setObjectName("sbStatusBar")
        MainWindow.setStatusBar(self.sbStatusBar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.bTurnLeft_2, QtCore.SIGNAL("pressed()"), MainWindow.on_turn_left)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Wubalubadubdub", None, -1))
        MainWindow.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Pickle Riiiiiick!", None, -1))
        self.bTurnLeft_2.setText(QtWidgets.QApplication.translate("MainWindow", "Turn Left", None, -1))
        self.bUp_2.setText(QtWidgets.QApplication.translate("MainWindow", "Up", None, -1))
        self.bTurnRight_2.setText(QtWidgets.QApplication.translate("MainWindow", "Turn Right", None, -1))
        self.bForward_2.setText(QtWidgets.QApplication.translate("MainWindow", "Forward", None, -1))
        self.bStrafeRight_2.setText(QtWidgets.QApplication.translate("MainWindow", "Strafe Right", None, -1))
        self.bShtrafeLeft_2.setText(QtWidgets.QApplication.translate("MainWindow", "Strafe Left", None, -1))
        self.bTakeOffLand_2.setText(QtWidgets.QApplication.translate("MainWindow", "TakeOff / Land", None, -1))
        self.bBack_2.setText(QtWidgets.QApplication.translate("MainWindow", "Back", None, -1))
        self.bDown_2.setText(QtWidgets.QApplication.translate("MainWindow", "Down", None, -1))
        self.bAddCommand.setText(QtWidgets.QApplication.translate("MainWindow", "Add Command", None, -1))
