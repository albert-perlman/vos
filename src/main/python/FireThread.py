from PyQt5.QtCore import *
from firebase import firebase


# VOS back-end thread for interaction with Firebase
#______________________________________________________________________________________________
class FireThread(QThread):

  # signals slotted to main thread
  finished = pyqtSignal(dict)
  setDisplayMsg = pyqtSignal(str)
  setAvailable = pyqtSignal(str)

  def __init__(self, oldData, tag=None, value=None, parent=None):
    super(FireThread, self).__init__(parent)

    self.oldData  = oldData
    self.tag      = tag
    self.value    = value

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

  def run(self):

    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    # READ
    if (self.value == None):
      for tag in self.tags:
        dataVal = db.get( '/VOS/' + tag, None )
        self.newData[tag] = dataVal

        if( dataVal != self.oldData[tag] ):

          if( tag == "t-available" ):
            self.setAvailable.emit( dataVal )

          elif( tag == "t-display" ):
            self.setDisplayMsg.emit( str(dataVal).strip('"').replace('\\n','<br/>') )
      
      self.finished.emit(self.newData)

    # WRITE
    elif ( self.tag and self.value ):
      db.patch( "/VOS/", { self.tag : '\"' + self.value + '\"' } )

