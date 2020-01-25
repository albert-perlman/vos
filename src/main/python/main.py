from fbs_runtime.application_context.PyQt5 import ApplicationContext

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia  import *

import os
import sys

from PyStyle import *

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
    self.setMinimumSize(self.maxScreenWidth//2.5,self.maxScreenHeight//2.5)
    self.resize(self.maxScreenWidth//2,self.maxScreenHeight//2)

    #############
    #  WIDGETS  #
    #############

    # status bar #
    self.status = QStatusBar()
    self.status.setStyleSheet(StyleSheet.css("status"))
    self.setStatusBar(self.status)

    #############
    #  LAYOUTS  #
    #############

    ####################
    #  SIGNAL / SLOTS  #
    ####################
    self.resized.connect(self.SLOT_resized)

    ####################
    #     START-UP     #
    ####################
    self.updateTitle()
    self.show()

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
