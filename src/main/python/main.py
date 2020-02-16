import os
import sys
import time
import datetime
import subprocess

# PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

# CSS
from PyStyle import StyleSheet

# Firebase
import FireRead
import FireWrite

# Twilio
from twilio.rest import Client
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
TWILIO_RECVR  = os.environ['TWILIO_RECVR']
ACCOUNT_SID   = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN    = os.environ['TWILIO_AUTH_TOKEN']

em = 1

class MainWindow(QMainWindow):
  resized = pyqtSignal()
  
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    # remove Minimize, Maximize, and Close buttons from application window
    self.setWindowFlags(self.windowFlags() | Qt.CustomizeWindowHint)
    self.setWindowFlags( self.windowFlags() &
                         ~Qt.WindowMaximizeButtonHint & 
                         ~Qt.WindowMinimizeButtonHint &
                         ~Qt.WindowCloseButtonHint )


    # initialize Twilio Client
    self.twilio = Client( ACCOUNT_SID, AUTH_TOKEN )

    # Main Widget Container
    MainWidgetContainer = QWidget()
    QFontDatabase.addApplicationFont('src/main/resources/base/fonts/Montserrat-Bold.ttf')
    QFontDatabase.addApplicationFont('src/main/resources/base/fonts/Montserrat-Regular.ttf')
    MainWidgetContainer.setStyleSheet(StyleSheet.css("window"))
    self.setCentralWidget(MainWidgetContainer)

    # get user's screen dimensions
    self.screenSize = QDesktopWidget().screenGeometry()
    self.maxScreenWidth = self.screenSize.width()
    self.maxScreenHeight = self.screenSize.height()

    # Main Window sizing
    self.setMinimumSize(1024*em, 600*em)
    self.resize(1024*em, 600*em)

    #############
    #  WIDGETS  #
    #############

    # clock #
    self.clock = QLabel( time.strftime("%H"+":"+"%M") )
    self.clock.setAlignment(Qt.AlignRight)
    self.clock.setFixedWidth(300*em)
    self.clock.setStyleSheet( StyleSheet.css("clock") )
    self.clockSpacer = QLabel() # spacer
    self.clockSpacer.setStyleSheet( StyleSheet.css("spacer") )
    self.clockSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    # date
    self.date = QLabel( datetime.datetime.now().strftime("%A, "+"%b. "+"%d") )
    self.date.setAlignment(Qt.AlignRight)
    self.date.setFixedWidth(300*em)
    self.date.setStyleSheet( StyleSheet.css("date") )

    # S&T Connect Browser #
    # self.webBtn = QPushButton("Schedule Appointment")
    # self.webBtn.setFixedHeight(50*em)
    # self.webBtn.setStyleSheet( StyleSheet.css("webBtn") )

    # QR Code #
    self.qr = QLabel(self)
    self.qr.setFixedSize(100*em,100*em)
    self.qr.move(715,10)
    self.qr.setStyleSheet(StyleSheet.css("qrCode"))
    pixmap = QPixmap('src/main/resources/base/images/qrcode-transparent.png')
    image = pixmap.scaled(100*em, 100*em, Qt.KeepAspectRatio, Qt.FastTransformation)
    self.qr.setPixmap(image)
    #labels
    self.qrTLabel = QLabel("SCAN ME", self)
    self.qrBLabel = QLabel("Schedule Appointment", self)
    self.qrBLabel.setFixedWidth(200*em)
    self.qrTLabel.move(715,-6)
    self.qrBLabel.move(665,96)
    self.qrTLabel.setAlignment(Qt.AlignCenter)
    self.qrBLabel.setAlignment(Qt.AlignCenter)
    self.qrTLabel.setStyleSheet(StyleSheet.css("qrLabel"))
    self.qrBLabel.setStyleSheet(StyleSheet.css("qrLabel"))

    # Office Hours #
    self.hours = QLabel("12:00 - 12:00")
    self.hours.setStyleSheet(StyleSheet.css("hours"))
    self.hours.setFixedWidth(self.clock.width())
    #label
    self.hoursLabel = QLabel("Office Hours")
    self.hoursLabel.setFixedWidth(self.hours.width())
    self.hoursLabel.setStyleSheet( StyleSheet.css("hoursLabel") )
    self.hoursSpacer = QLabel() # spacer
    self.hoursSpacer.setStyleSheet( StyleSheet.css("spacer") )
    self.hoursSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum) 

    # Available / Unavailable #
    self.available = QLabel("UNAVAILABLE")
    self.available.setFixedSize(250*em, 50*em)
    self.available.setAlignment(Qt.AlignCenter)
    self.available.setStyleSheet( StyleSheet.css("unavailable") )

    # Display Message #
    self.displayMsg = QTextEdit()
    self.displayMsg.setFixedSize(800*em, 100*em)
    self.displayMsg.setText("No messages")
    self.displayMsg.setReadOnly(True)
    self.displayMsg.setAlignment(Qt.AlignCenter)
    self.displayMsg.setStyleSheet( StyleSheet.css("displayMsg") )
    # last modified label
    self.displayMsgUpdate = QLabel(self)
    self.displayMsgUpdate.setFixedWidth(200*em)
    self.displayMsgUpdate.move(160,120)
    self.displayMsgUpdate.setStyleSheet(StyleSheet.css("displayMsgUpdate"))

     # S&T Logo #
    self.logoLabel = QLabel(self)
    self.logoLabel.move(335, 240)
    self.logoLabel.setFixedSize(400*em, 100*em)
    pixmap = QPixmap('src/main/resources/base/images/MissouriS&T_Horizontal_DigitalMinerGreen.png')
    image = pixmap.scaled(400*em, 60*em, Qt.KeepAspectRatio, Qt.FastTransformation)
    self.logoLabel.setPixmap(image)

    # Student Message Selections #
    self.studentMsgList = [
      "I have a question about class.",
      "I am here for our meeting.",
      "I need to cancel our meeting.",
      "When are you available to meet today?",
      "Yes",
      "No",
      "OK"
    ]
    self.studentMsgSel = []
    for msg in self.studentMsgList:
      btn = QPushButton(msg)
      btn.setCheckable(True)
      btn.setChecked(False)
      btn.setFixedHeight(65*em)
      btn.setStyleSheet( StyleSheet.css("studentMsgSel") )
      self.studentMsgSel.append(btn)
      if( msg == self.studentMsgList[4] or msg == self.studentMsgList[5] or msg == self.studentMsgList[6] ):
        btn.setFixedWidth(100*em)

    # Student Name #
    self.studentName = LineEdit()
    self.studentNameLabel = QLabel("Name")
    self.studentNameLabel.setAlignment(Qt.AlignRight)
    self.studentName.setFixedSize(241*em, 40*em)
    self.studentNameLabel.setFixedSize(80*em, 30*em)
    self.studentName.setStyleSheet(StyleSheet.css("studentName"))
    self.studentNameLabel.setStyleSheet( StyleSheet.css("studentNameLabel") )

    # Send Message #
    self.sendMsgBtn = QPushButton()
    self.sendMsgBtn.setText("Send Message")
    self.sendMsgBtn.setFixedSize(200*em, 40*em)
    self.sendMsgBtn.setStyleSheet( StyleSheet.css("sendMsgBtn") )
    self.sendMsgSpacer = QLabel() # spacer
    self.sendMsgSpacer.setStyleSheet( StyleSheet.css("spacer") )
    self.sendMsgSpacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

    # Conversation Display #
    self.convoText = QTextEdit()
    self.convoText.setReadOnly(True)
    self.convoText.setStyleSheet( StyleSheet.css("convoText") )

    # clear convo history button #
    self.convoClear = QPushButton("clear chat")
    self.convoClear.setStyleSheet( StyleSheet.css("button") )

    # status bar #
    self.status = QStatusBar()
    self.status.setStyleSheet( StyleSheet.css("status") )
    self.setStatusBar(self.status)

    #############
    #  LAYOUTS  #
    #############

    # main vertical container layout
    MainVLayout = QVBoxLayout(MainWidgetContainer)


    # TOP BAR
    #__________________________________________________________________________

    # office hours
    HoursVLayout = QVBoxLayout()
    HoursVLayout.addWidget(self.hours)
    HoursVLayout.addWidget(self.hoursLabel)

    # clock / date
    ClockVLayout = QVBoxLayout()
    ClockVLayout.addWidget(self.clock)
    ClockVLayout.addWidget(self.date)

    # top info bar
    TopHLayout = QHBoxLayout()
    TopHLayout.setAlignment(Qt.AlignCenter)
    TopHLayout.addLayout(HoursVLayout)
    TopHLayout.addWidget(self.hoursSpacer)
    TopHLayout.addWidget(self.available)
    # TopHLayout.addWidget(self.webBtn)
    TopHLayout.addWidget(self.clockSpacer)
    TopHLayout.addLayout(ClockVLayout)

    #__________________________________________________________________________

    # display message
    DisplayMsgHLayout = QHBoxLayout()
    DisplayMsgHLayout.setAlignment(Qt.AlignCenter)
    DisplayMsgHLayout.addWidget(self.displayMsg)

    # clear history
    ClearConvoHLayout = QHBoxLayout()
    ClearConvoHLayout.setAlignment(Qt.AlignRight)
    ClearConvoHLayout.addWidget(self.convoClear)


    # STUDENT MESSAGING
    #__________________________________________________________________________

    # Main Messaging Layout
    MsgCenterVLayout = QVBoxLayout()
    MsgCenterHLayout = QHBoxLayout()

    # Group Box
    self.msgGroupBox = QGroupBox("Message Center")
    self.msgGroupBox.setAlignment(Qt.AlignLeft)
    self.msgGroupBox.setStyleSheet( StyleSheet.css("msgGroupBox") )
    self.msgGroupBox.setLayout(MsgCenterVLayout)

    # student messaging - SELECT
    StudentMsgSelHLayout1 = QHBoxLayout()
    StudentMsgSelHLayout2 = QHBoxLayout()
    StudentMsgSelHLayout1.setAlignment(Qt.AlignCenter)
    StudentMsgSelHLayout2.setAlignment(Qt.AlignCenter)
    for i in range(0,3):
      StudentMsgSelHLayout1.addWidget( self.studentMsgSel[i] )
    for i in range(3,7):
      StudentMsgSelHLayout2.addWidget( self.studentMsgSel[i] )

    # student messaging - SEND
    StudentMsgSendHLayout = QHBoxLayout()
    StudentMsgSendHLayout.setAlignment(Qt.AlignCenter)
    StudentMsgSendHLayout.addWidget(self.studentNameLabel)
    StudentMsgSendHLayout.addWidget(self.studentName)
    StudentMsgSendHLayout.addWidget(self.sendMsgSpacer)
    StudentMsgSendHLayout.addWidget(self.sendMsgBtn)

    # add layouts
    MsgCenterVLayout.addLayout(StudentMsgSelHLayout1)
    MsgCenterVLayout.addLayout(StudentMsgSelHLayout2)
    MsgCenterVLayout.addLayout(StudentMsgSendHLayout)
    MsgCenterHLayout.addWidget(self.msgGroupBox)
    MsgCenterHLayout.addWidget(self.convoText)

    #__________________________________________________________________________

    # add layouts and widgets
    MainVLayout.addLayout(TopHLayout)
    MainVLayout.addLayout(DisplayMsgHLayout)
    MainVLayout.addLayout(ClearConvoHLayout)
    MainVLayout.addLayout(MsgCenterHLayout)

    ####################
    #  SIGNAL / SLOTS  #
    ####################
    self.resized.connect(self.SLOT_resized)
    # self.webBtn.clicked.connect(self.SLOT_webBtnClicked)
    self.convoClear.clicked.connect(self.SLOT_convoClearClicked)
    self.studentName.focusIn.connect(self.SLOT_nameFocusIn)
    self.studentName.focusOut.connect(self.SLOT_nameFocusOut)
    self.sendMsgBtn.clicked.connect(self.SLOT_sendMsgBtnClicked)
    self.displayMsg.textChanged.connect(self.SLOT_displayMsgChanged)
    for btn in self.studentMsgSel:
      btn.clicked.connect(self.SLOT_studentMsgSelClicked)

    ####################
    #     START-UP     #
    ####################
    self.updateTitle()
    self.updateClock()
    self.show()

    # initialize dictionary to store Firebase data
    self.data = { 
      "t-display": "",
      "t-available": False,
      "t-name": "",
      "t-reply": "",
      "t-hours-start": "12:00",
      "t-hours-end": "12:00",
      "s-name": "",
      "s-msg": ""
    }

    # retreive Firebase data and update GUI 
    self.readFirebase()

    # refresh data timer
    # restarts every time FireRead thread finishes
    self.refreshTimer = QTimer(self)
    self.refreshTimer.setSingleShot(True)
    self.refreshTimer.timeout.connect(self.readFirebase)

    # clock timer
    # repeats infinitely to trigger clock updates every 5 seconds
    clockTimer = QTimer(self)
    clockTimer.timeout.connect(self.updateClock)
    clockTimer.start(5000)

  # spawn FireRead thread to read data values for all tags stored in Firebase
  # called cyclically by refreshTimer
  def readFirebase(self):

    # create Firebase data retrieval thread
    self.FireRead = FireRead.FireRead(self.data)

    # connect signals
    self.FireRead.setAvailable.connect(self.SLOT_availabilityChanged)
    self.FireRead.setHours.connect(self.SLOT_hoursChanged)
    self.FireRead.setTeacherName.connect(self.updateTitle)
    self.FireRead.setTeacherReply.connect(self.SLOT_teacherReply)
    self.FireRead.setDisplayMsg.connect(self.displayMsg.setText)
    self.FireRead.finished.connect(self.SLOT_threadFinished)

    # run Firebase thread
    self.FireRead.start()

  # spawn FireWrite thread to store data values for given tags in Firebase
  def writeFirebase(self, tags, values):

     # create Firebase data retrieval thread
    self.FireWrite = FireWrite.FireWrite( tags, values )

    # run Firebase thread
    self.FireWrite.start()

  # send SMS message from Twilio
  def sendSMS(self, msg):
    self.twilio.messages.create( to=TWILIO_RECVR,
                                 from_=TWILIO_NUMBER, 
                                 body=msg )

  # re-format 24-hour time string (e.g. 13:00) to 12-hour time (e.g. 1:00pm)
  def formatTime(self, t):
    t = t.split(':')
    hour = int(t[0])
    am_pm = "am"
    
    if( hour > 12 ):
      t[0] = str( hour - 12 )
    if( hour >= 12 ):
      am_pm= "pm"

    return( t[0] + ":" + t[1] + am_pm )

  # SLOT: teacher availability changed
  def SLOT_availabilityChanged(self, availability):
    if( "true" == availability ):
      self.available.setText("AVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("available"))
    elif( "false" == availability ):
      self.available.setText("UNAVAILABLE")
      self.available.setStyleSheet(StyleSheet.css("unavailable"))

  # SLOT: teacher office hours changed
  def SLOT_hoursChanged(self, startTime, endTime):
    startTime = self.formatTime(startTime)
    endTime = self.formatTime(endTime)

    self.hours.setText( startTime + " - " + endTime )

  # PyQtWebEngine currently not supported on pi
  # # SLOT: schedule appointment button clicked - open browser to S&T Connect
  # def SLOT_webBtnClicked(self):
    # self.web = QWebEngineView()
    # self.web.page().profile().cookieStore().deleteAllCookies()
    # self.web.setUrl( QUrl("https://mst.starfishsolutions.com/starfish-ops/instructor/serviceCatalog.html?tenantId=594#/") )
    # self.web.setFixedSize(1024*em, 600*em)
    # self.web.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
    # self.web.setWindowFlag(Qt.WindowMinimizeButtonHint, False)
    # self.web.show()

  # SLOT: student name line edit focused - open keyboard
  def SLOT_nameFocusIn(self):
    self.keyboard = subprocess.Popen('matchbox-keyboard', stdout=subprocess.PIPE)
    self.studentName.setFocus()

  # SLOT: student name line edit lost focus - close keyboard
  def SLOT_nameFocusOut(self):
    self.keyboard.kill()

  # SLOT: send student message button clicked
  def SLOT_sendMsgBtnClicked(self):
    if( self.studentName.text() ):
      for btn in self.studentMsgSel:
        if ( btn.isChecked() ):
          self.sendSMS( self.studentName.text() + ": " + btn.text() )
          self.writeFirebase( ["s-name", "s-msg"], [self.studentName.text(), btn.text()] )
          self.convoText.append( StyleSheet.msgHTML +
                                 StyleSheet.timestampHTML + self.clock.text() + "\t" + "</span>" +
                                 StyleSheet.studentNameHTML + self.studentName.text() + ":"  + "</span> " +
                                 btn.text() + "</p>")
          self.status.showMessage( "Sent message: " + btn.text() )
          break

      for btn in self.studentMsgSel:
        btn.setChecked(False)
    else:
      self.status.showMessage("Failed to send message! Please enter a name.")

  # SLOT: student message selection clicked
  def SLOT_studentMsgSelClicked(self):
    for btn in self.studentMsgSel:
      if( btn != self.sender() ):
        btn.setChecked(False)
    if( not self.sender().isChecked() ):
      self.sender().setChecked(False)

  # SLOT: teacher reply received
  def SLOT_teacherReply(self, reply):
    self.sendSMS( self.windowTitle() + ": " + reply )
    self.convoText.append( StyleSheet.msgHTML + 
                           StyleSheet.timestampHTML + self.clock.text() + "\t" + "</span>" +
                           StyleSheet.teacherNameHTML + self.windowTitle() + ":"  + "</span> " +
                           reply + "</p>" )

  # SLOT: clear chat button clicked
  def SLOT_convoClearClicked(self):
   msgBox = QMessageBox()
   msgBox.setWindowTitle("V.O.S.")
   msgBox.setText('Are sure you want to clear your chat history?')
   msgBox.addButton(QPushButton('Yes'), QMessageBox.YesRole)
   msgBox.addButton(QPushButton('No'), QMessageBox.NoRole)
   ret = msgBox.exec_()

   if( ret == 0 ):
    self.convoText.clear()

  # SLOT: firebase data retrieval thread finished
  def SLOT_threadFinished(self, newData):
    self.data = newData
    self.refreshTimer.start(2500)

  # SLOT: Display Message changed - reset text alignment
  def SLOT_displayMsgChanged(self):
    try:
      self.displayMsgUpdate.setText("updated " + datetime.datetime.now().strftime("%b. "+"%d at "+ self.clock.text() ) )
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
    self.setWindowTitle( str )

  # update clock display
  def updateClock(self):
    currentTime = time.strftime("%H"+":"+"%M").split(':')
    hour = int(currentTime[0])
    am_pm = "am"
    if( hour > 12 ):
      currentTime[0] = str( hour - 12 )
    if( hour >= 12 ):
      am_pm = "pm"
    
    self.clock.setText( currentTime[0] + ":" + currentTime[1] + am_pm )
    self.updateDate()

  # update date display
  def updateDate(self):
    self.date.setText( datetime.datetime.now().strftime("%A, "+"%b. "+"%d") )

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

# overide QLineEdit Focus Events to emit signals
class LineEdit(QLineEdit):
  focusIn = pyqtSignal()
  focusOut = pyqtSignal()
  def focusInEvent(self, event):
    self.focusIn.emit()
  def focusOutEvent(self, event):
    self.focusOut.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    sys.exit(app.exec_())
