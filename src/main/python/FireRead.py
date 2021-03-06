from PyQt5.QtCore import *
from firebase import firebase

# VOS back-end thread for Firebase reads
#______________________________________________________________________________________________
class FireRead(QThread):

  # signals slotted to main thread
  finished = pyqtSignal(dict)
  setTeacherName  = pyqtSignal(str)
  setTeacherReply = pyqtSignal(str)  
  setDisplayMsg   = pyqtSignal(str)
  setAvailable    = pyqtSignal(str)
  setHours        = pyqtSignal(str, str)

  def __init__(self, oldData, parent=None):
    super(FireRead, self).__init__(parent)

    self.oldData = oldData

    self.tags = { 
      "t-display",
      "t-available",
      "t-name",
      "t-reply",
      "t-hours-start",
      "t-hours-end",
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
      "s-name": "",
      "s-msg": ""
    }

  def run(self):

    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    # READ data for all tags
    for tag in self.tags:
      dataVal = db.get( '/VOS/' + tag, None )
      self.newData[tag] = dataVal

      # if the data has changed since last read
      if( dataVal != self.oldData[tag] or tag == "t-reply" ):

        if( tag == "t-name" ):
          self.setTeacherName.emit( str(dataVal).strip('"') )

        elif( tag == "t-available" ):
          self.setAvailable.emit( dataVal )

        elif( tag == "t-hours-start" ):
          endTime = db.get( '/VOS/' + "t-hours-end", None )
          self.setHours.emit( str(dataVal).strip('"'), str(endTime).strip('"') )

        elif( tag == "t-hours-end" ):
          startTime = db.get( '/VOS/' + "t-hours-start", None )
          self.setHours.emit( str(startTime).strip('"'), str(dataVal).strip('"') )

        elif( tag == "t-display" ):
          self.setDisplayMsg.emit( str(dataVal).strip('"').replace('\\n','<br/>') )
        
        elif( tag == "t-reply" ):
          reply = str(dataVal).strip('"').replace('\\n','<br/>')
          if( reply ):
            self.setTeacherReply.emit( reply )
          db.patch( "/VOS/", { tag : '\"' + '' + '\"' } )
      
    self.finished.emit(self.newData)
