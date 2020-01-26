from PyQt5.QtCore import *
from firebase import firebase


# VOS back-end thread for interaction with Firebase
#______________________________________________________________________________________________
class FireThread(QThread):

  # signals slotted to main thread
  finished = pyqtSignal()
  setDisplayMsg = pyqtSignal(str)
  setAvailable = pyqtSignal(str)

  def __init__(self, displayMsg, parent=None):
    super(FireThread, self).__init__(parent)

    self.sem = QSemaphore() # semaphore used for blocking thread during GUI updates in main thread
    self.tags = { "t-display",
                  "t-available",
                  "t-name",
                  "t-reply",
                  "t-hours-start",
                  "t-hours-end",
                  "t-minutes-start",
                  "t-minutes-end",
                  "s-name",
                  "s-msg" }

    self.displayMsg = displayMsg

  def run(self):

    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    for tag in self.tags:
      data = db.get( '/VOS/' + tag, None )

      if( tag == "t-available" ):
        self.setAvailable.emit( data )

      elif( tag == "t-display" ):
        text = str(data).strip('"').replace('\\n','<br/>')
        if( text != str(self.displayMsg) ):
          self.setDisplayMsg.emit( str(data).strip('"').replace('\\n','<br/>') )
    
    self.finished.emit()
