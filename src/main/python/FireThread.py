from PyQt5.QtCore import *
from firebase import firebase


# VOS back-end thread for interaction with Firebase
#______________________________________________________________________________________________
class FireThread(QThread):

  # signals slotted to main thread
  finished = pyqtSignal(dict)
  setDisplayMsg = pyqtSignal(str)
  setAvailable = pyqtSignal(str)

  def __init__(self, oldData, parent=None):
    super(FireThread, self).__init__(parent)

    self.sem = QSemaphore() # semaphore used for blocking thread during GUI updates in main thread
    self.tags = { 
      "t-display",
      "t-available",
      "t-name",
      "t-reply",
      "t-hours-start",
      "t-hours-end",
      "t-minutes-start",
      "t-minutes-end",
      "s-name",
      "s-msg"
    }

    self.newData = { 
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

    self.oldData = oldData

  def run(self):

    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    for tag in self.tags:
      dataVal = db.get( '/VOS/' + tag, None )
      self.newData[tag] = dataVal

      if( dataVal != self.oldData[tag] ):

        if( tag == "t-available" ):
          self.setAvailable.emit( dataVal )

        elif( tag == "t-display" ):
          print("heyooo\n---\n")
          self.setDisplayMsg.emit( str(dataVal).strip('"').replace('\\n','<br/>') )
    
    self.finished.emit(self.newData)
