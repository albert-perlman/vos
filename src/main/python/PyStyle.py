# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):
  def __init__(self, arg):
    super(StyleSheet, self).__init__()
    self.arg = arg
    
  def css(widget=None):

    if ("window" == widget):

        css = \
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

        return css

    elif ("button" == widget):

        css = \
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

        return css

    elif ("displayMsg" == widget):

        css = \
        "QTextEdit {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(75,75,75);" + \
        "border-radius:10px;" + \
        "}"

        return css

    elif ("clock" == widget):

        css = \
        "QLabel {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:transparent;" + \
        "}"
        
        return css

    elif ("hours" == widget):

        css = \
        "QLabel {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:transparent;" + \
        "}"

        return css

    elif ("hoursLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size:20px;" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:transparent;" + \
        "}"

        return css

    elif ("available" == widget):

        css = \
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

        return css

    elif ("unavailable" == widget):

        css = \
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

        return css

    elif ("studentMsgSel" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 16px; font-weight:bold;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(40,40,40);" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "padding:5px;" + \
        "}" + \
        "QPushButton::hover {" + \
        "background-color:rgb(60,60,60);" + \
        "}" + \
        "QPushButton:checked {" + \
        "background-color: rgb(60,60,60);" + \
        "border: 5px solid black; }"

        return css


    elif ("studentName" == widget):

        css = \
        "QLineEdit {" + \
        "font-size: 16px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:rgb(150,150,150);" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "padding:5px;" + \
        "}"

        return css


    elif ("studentNameLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size: 16px; font-weight:bold;" + \
        "color:rgb(255,255,255);" + \
        "background-color:transparent;" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "padding:0px;" + \
        "}"

        return css

    elif ("status" == widget):

        css = \
        "QStatusBar {" + \
        "font-family:Cantarell;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(75,75,75);" + \
        "}"

        return css

    elif ("spacer" == widget):

        css = \
        "QLabel {" + \
        "background-color:transparent;" + \
        "}"

        return css
