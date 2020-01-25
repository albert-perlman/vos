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

    elif ("button" == widget):

        button = \
        "QPushButton {" + \
        "font-size: 16px; font-weight:bold;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(50,50,50);" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "padding:5px;" + \
        "}" + \
        "QPushButton::hover {" + \
        "background-color:rgb(60,60,60);" + \
        "}"

        return button

    elif ("displayMsg" == widget):

        displayMsg = \
        "QTextEdit {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(75,75,75);" + \
        "border-radius:10px;" + \
        "}"

        return displayMsg

    elif ("available" == widget):

        available = \
        "QLabel {" + \
        "font-size:20px;" + \
        "font-weight:bold;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
        "background-color:" + \
        "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," + \
        "stop: 0.0 rgb(50,255,50)," + \
        "stop: 1.0 rgb(150,255,150));" + \
        "border: 3px ridge black;" + \
        "border-radius:10px;" + \
        "}"

        return available

    elif ("unavailable" == widget):

        unavailable = \
        "QLabel {" + \
        "font-size:20px;" + \
        "font-weight:bold;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
        "background-color:" + \
        "qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1," + \
        "stop: 0.0 rgb(255,50,50)," + \
        "stop: 1.0 rgb(255,150,150));" + \
        "border: 3px ridge black;" + \
        "border-radius:10px;" + \
        "}"

        return unavailable

    elif ("status" == widget):

        StatusBar = \
        "QStatusBar {" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(75,75,75);" + \
        "}"

        return StatusBar
