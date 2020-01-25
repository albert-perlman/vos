from PyQt5.QtCore import *
from firebase import firebase


# VOS back-end thread for interaction with Firebase
#______________________________________________________________________________________________
class FireThread(QThread):

  # signals slotted to main thread
  finished = pyqtSignal()
  setDisplayMsg = pyqtSignal(str)
  setAvailable = pyqtSignal(str)

  def __init__(self, parent=None):
    super(FireThread, self).__init__(parent)

    self.sem = QSemaphore() # semaphore used for blocking thread during GUI updates in main thread
    self.tags = {"teacher/display", "teacher/available"}
      
  def run(self):
    
    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    for tag in self.tags:
      data = db.get( '/VOS/' + tag, None )

      if( tag == "teacher/available" ):
        self.setAvailable.emit( data )

      elif( tag == "teacher/display" ):
        self.setDisplayMsg.emit( str(data).strip('"').replace('\\n','<br/>') )
    
    self.finished.emit()
