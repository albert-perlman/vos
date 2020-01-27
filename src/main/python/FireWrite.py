from PyQt5.QtCore import *
from firebase import firebase

# VOS back-end thread for Firebase writes
#______________________________________________________________________________________________
class FireWrite(QThread):

  def __init__(self, tags=None, values=None, parent=None):
    super(FireWrite, self).__init__(parent)

    self.tags   = tags
    self.values = values

  def run(self):

    dbURL = "https://v-o-s-62a4d.firebaseio.com/VOS"
    db = firebase.FirebaseApplication(dbURL, None)

    # WRITE data values for given tags
    for tag, value in zip( self.tags, self.values ):
      db.patch( "/VOS/", { tag : '\"' + value + '\"' } )

