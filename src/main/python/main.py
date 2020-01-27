from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia  import *

import os
import sys
import time

from PyStyle import StyleSheet
import FireThread

em = 1

class MainWindow(QMainWindow):
  resized = pyqtSignal()
  
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    self.appctxt = ApplicationContext()

    # Main Widget Container
    MainWidgetContainer = QWidget()
    QFontDatabase.addApplicationFont(self.appctxt.get_resource('fonts/Cantarell-Regular.ttf'))
    MainWidgetContainer.setStyleSheet(StyleSheet.css("window"))
    self.setCentralWidget(MainWidgetContainer)

    # get user's screen dimensions
    self.screenSize = QDesktopWidget().screenGeometry()
    self.maxScreenWidth = self.screenSize.width()
    self.maxScreenHeight = self.screenSize.height()

    # Main Window sizing
    self.setMinimumSize(1024*em,600*em)
    self.resize(1024*em,600*em)

    #############
    #  WIDGETS  #
    #############

   # self.startBtn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    # Available / Unavailable #
    self.available = QLabel("UNAVAILABLE")
    self.available.setFixedSize(250*em,50*em)
    self.available.setAlignment(Qt.AlignCenter)
    self.available.setStyleSheet(StyleSheet.css("unavailable"))

    # Display Message #
    self.displayMsg = QTextEdit()
    self.displayMsg.setFixedSize(800*em, 90*em)
    self.displayMsg.setText("No messages")
    self.displayMsg.setReadOnly(True)
    self.displayMsg.setAlignment(Qt.AlignCenter)
    self.displayMsg.setStyleSheet(StyleSheet.css("displayMsg"))

    # Student Message Selections #
    self.studentMsgList = [
      "I am here for our meeting.",
      "I have a question about class.",
      "When are you available to meet today?",
    ]
    self.studentMsgSel = []
    for msg in self.studentMsgList:
      btn = QPushButton(msg)
      btn.setCheckable(True)
      btn.setFixedSize(300*em, 100*em)
      btn.setStyleSheet(StyleSheet.css("button"))
      self.studentMsgSel.append(btn)

    # Send Message #
    self.sendMsgBtn = QPushButton()
    self.sendMsgBtn.setText("Send Message to ")
    self.sendMsgBtn.setFixedSize(400*em, 60*em)
    self.sendMsgBtn.setStyleSheet(StyleSheet.css("button"))

    # Refresh Button #
    self.refreshBtn = QPushButton()
    self.refreshBtn.setText("@")
    self.refreshBtn.setStyleSheet(StyleSheet.css("button"))

    # status bar #
    self.status = QStatusBar()
    self.status.setStyleSheet(StyleSheet.css("status"))
    self.setStatusBar(self.status)

    #############
    #  LAYOUTS  #
    #############

    # main vertical container layout
    MainVLayout = QVBoxLayout(MainWidgetContainer)

    # top info bar
    TopHLayout = QHBoxLayout()
    TopHLayout.setAlignment(Qt.AlignCenter)
    TopHLayout.addWidget(self.available)

    # display message
    DisplayMsgHLayout = QHBoxLayout()
    DisplayMsgHLayout.setAlignment(Qt.AlignCenter)
    DisplayMsgHLayout.addWidget(self.displayMsg)

    # student messaging - SELECT
    StudentMsgSelHLayout = QHBoxLayout()
    StudentMsgSelHLayout.setAlignment(Qt.AlignCenter)
    for btn in self.studentMsgSel:
      StudentMsgSelHLayout.addWidget(btn)

    # student messaging -SEND
    StudentMsgSendHLayout = QHBoxLayout()
    StudentMsgSendHLayout.setAlignment(Qt.AlignCenter)
    StudentMsgSendHLayout.addWidget(self.sendMsgBtn)    

    # bottom info bar
    BottomHLayout = QHBoxLayout()
    BottomHLayout.setAlignment(Qt.AlignRight)
    BottomHLayout.addWidget(self.refreshBtn)

    # add layouts and widgets
    MainVLayout.addLayout(TopHLayout)
    MainVLayout.addLayout(DisplayMsgHLayout)
    MainVLayout.addLayout(StudentMsgSelHLayout)
    MainVLayout.addLayout(StudentMsgSendHLayout)
    MainVLayout.addLayout(BottomHLayout)

    ####################
    #  SIGNAL / SLOTS  #
    ####################
    self.resized.connect(self.SLOT_resized)
    self.refreshBtn.clicked.connect(self.SLOT_refreshBtnClicked)
    self.sendMsgBtn.clicked.connect(self.SLOT_sendMsgBtnClicked)
    self.displayMsg.textChanged.connect(self.SLOT_displayMsgChanged)
    for btn in self.studentMsgSel:
      btn.clicked.connect(self.SLOT_studentMsgSelClicked)

    ####################
    #     START-UP     #
    ####################
    self.updateTitle()
    self.show()

    # initialize dictionary to store Firebase data
    self.data = { 
      "t-display": "",
      "t-available": False,
      "t-name": "",
      "t-reply": "",
      "t-hours-start": "",
      "t-hours-end": "",
      "t-minutes-start": "",
      "t-minutes-end": "",
      "s-name": "",
      "s-msg": ""
    }

    # refresh data timer
    # repeats infinitely to trigger data retrieval from Firebase
    refreshTimer = QTimer(self)
    refreshTimer.timeout.connect(self.readFirebase)
    refreshTimer.start(5000)


  # spawn FireThread to read data values for all tags stored in Firebase
  # called cyclically by refreshTimer
  def readFirebase(self):

     # create Firebase data retrieval thread
    self.FireThread = FireThread.FireThread(self.data)

    # connect signals
    self.FireThread.setAvailable.connect(self.SLOT_availabilityChanged)
    self.FireThread.setTeacherName.connect(self.updateTitle)
    self.FireThread.setDisplayMsg.connect(self.displayMsg.setText)
    self.FireThread.finished.connect(self.SLOT_threadFinished)

    # run Firebase thread
    self.FireThread.start()

  # spawn FireThread to write data value for given tag in Firebase
  def writeFirebase(self, tag, value):

     # create Firebase data retrieval thread
    self.FireThread = FireThread.FireThread( self.data, tag, value )

    # run Firebase thread
    self.FireThread.start()

  # SLOT: teacher availability changed
  def SLOT_availabilityChanged(self, availability):
    if( "true" == availability ):
      self.available.setText("AVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("available"))
    elif( "false" == availability ):
      self.available.setText("UNAVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("unavailable"))

  # SLOT: send student message button clicked
  def SLOT_sendMsgBtnClicked(self):
    pass

  # SLOT: student message selection clicked
  def SLOT_studentMsgSelClicked(self):
    msg = self.sender().text()
    self.writeFirebase("s-msg", msg)

  # SLOT: refresh button clicked - retrieve data from Firebase
  def SLOT_refreshBtnClicked(self):
    self.readFirebase()

  # SLOT: firebase data retrieval thread finished
  def SLOT_threadFinished(self, newData):
    self.data = newData

  # SLOT: Display Message changed
  def SLOT_displayMsgChanged(self):
    try:
      self.displayMsg.setAlignment(Qt.AlignCenter)
    except:
      pass

  # SLOT: Main Window has been resized
  def SLOT_resized(self):
    pass

  # critical dialog pop-up
  def dialogCritical(self, s):
    dlg = QMessageBox(self)
    dlg.setText(s)
    dlg.setIcon(QMessageBox.Critical)
    dlg.show()

  # delete all widgets in a layout
  def clearLayout(self, layout):
    while layout.count():
      child = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()

  # update main window title
  def updateTitle(self, str=""):
    self.setWindowTitle(""+ str)

  # map key press events to gallery navigation
  def keyPressEvent(self, event):

    keyCode = event.key()

    # map left / right arrow keys
    if (16777234 == keyCode):   # left arrow
      pass
    elif (16777236 == keyCode): # right arrow
      pass

    try: # map 0-9 key press
      if (49 == keyCode):   # 1
        pass
      elif (50 == keyCode): # 2
        pass
      elif (51 == keyCode): # 3
        pass
      elif (52 == keyCode): # 4
        pass
      elif (53 == keyCode): # 5
        pass
      elif (54 == keyCode): # 6
        pass
      elif (55 == keyCode): # 7
        pass
      elif (56 == keyCode): # 8
        pass
      elif (57 == keyCode): # 9
        pass
      elif (48 == keyCode): # 0
        pass
    except:
      pass                                       

  # overload Main Window resizeEvent to emit signal
  def resizeEvent(self, event):
    self.resized.emit()
    return super(MainWindow, self).resizeEvent(event)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    Window = MainWindow()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)
