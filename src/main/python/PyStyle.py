# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):
  def __init__(self, arg):
    super(ClassName, self).__init__()
    self.arg = arg
    
  def css(widget=None):

    if ("window" == widget):

        MainWindow = \
        "QWidget {" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:" + \
        "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," + \
        "stop: 0.0 rgb(35,35,35)" + \
        "stop: 0.2 rgb(50,50,50)" + \
        "stop: 0.7 rgb(50,50,50)," + \
        "stop: 1.0 rgb(25,25,25));" + \
        "}"

        return MainWindow

    elif ("status" == widget):

        StatusBar = \
        "QStatusBar {" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(75,75,75);" + \
        "}"

        return StatusBar
