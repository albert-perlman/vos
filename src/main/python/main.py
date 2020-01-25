from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia  import *

import os
import sys

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

    # bottom info bar
    BottomHLayout = QHBoxLayout()
    BottomHLayout.setAlignment(Qt.AlignRight)
    BottomHLayout.addWidget(self.refreshBtn)

    # add layouts and widgets
    MainVLayout.addLayout(TopHLayout)
    MainVLayout.addLayout(DisplayMsgHLayout)
    MainVLayout.addLayout(BottomHLayout)

    ####################
    #  SIGNAL / SLOTS  #
    ####################
    self.resized.connect(self.SLOT_resized)
    self.refreshBtn.clicked.connect(self.SLOT_refreshBtnClicked)
    self.displayMsg.textChanged.connect(self.SLOT_displayMsgChanged)

    ####################
    #     START-UP     #
    ####################
    self.updateTitle()
    self.show()

    timer = QTimer(self)
    timer.timeout.connect(self.SLOT_refreshBtnClicked)
    timer.start(2000)


  # read data value for given tag stored in Firebase
  def readFirebase(self):

     # create Firebase data retrieval thread
    self.FireThread = FireThread.FireThread()

    # run Firebase thread
    self.FireThread.start()
    self.FireThread.setAvailable.connect(self.SLOT_availabilityChanged)
    self.FireThread.setDisplayMsg.connect(self.displayMsg.setText)
    self.FireThread.finished.connect(self.SLOT_threadFinished)


  def SLOT_availabilityChanged(self, availability):
    if( "true" == availability ):
      self.available.setText("AVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("available"))
    elif( "false" == availability ):
      self.available.setText("UNAVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("unavailable"))

  # SLOT: refresh button clicked - retrieve data from Firebase
  def SLOT_refreshBtnClicked(self):
    self.readFirebase()

  # SLOT: thread finished
  def SLOT_threadFinished(self):
    pass

  # SLOT: display Message changed
  def SLOT_displayMsgChanged(self):
    self.displayMsg.setAlignment(Qt.AlignCenter)

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
    self.setWindowTitle("V\tO\tS"+ str)

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
