# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):

  studentNameHTML = "<span style=\" color:#0000FF;\" >"
  teacherNameHTML = "<span style=\" color:#FF00BB;\" >"

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
        "stop: 0.0 rgb(200,200,200)" + \
        "stop: 0.2 rgb(240,240,240)" + \
        "stop: 0.7 rgb(240,240,240)," + \
        "stop: 1.0 rgb(200,200,200));" + \
        "}"

        return css

    elif ("button" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 14px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:2px solid black;" + \
        "border-radius:0px;" + \
        "padding:5px;" + \
        "}" + \
        "QPushButton::hover {" + \
        "background-color:white;" + \
        "}" + \
        "QPushButton::pressed {" + \
        "color: white;" + \
        "background-color:rgb(50,50,50);" + \
        "}"

        return css

    elif ("sendMsgBtn" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 20px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:2px solid black;" + \
        "border-radius:0px;" + \
        "padding:5px;" + \
        "}" + \
        "QPushButton::hover {" + \
        "background-color:white;" + \
        "}" + \
        "QPushButton::pressed {" + \
        "color: white;" + \
        "background-color:rgb(50,50,50);" + \
        "}"

        return css

    elif ("displayMsg" == widget):

        css = \
        "QTextEdit {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
        "background-color:rgb(200,200,200);" + \
        "border-radius:0px;" + \
        "}"

        return css

    elif ("clock" == widget):

        css = \
        "QLabel {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "}"
        
        return css

    elif ("hours" == widget):

        css = \
        "QLabel {" + \
        "font-size:26px;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "}"

        return css

    elif ("hoursLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size:20px;" + \
        "font-family:Cantarell;" + \
        "color:black;" + \
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

    elif ("msgGroupBox" == widget):

        css = \
        "QGroupBox {" + \
        "font-size: 22px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:0px solid black;" + \
        "border-radius:0px;" + \
        "padding-top:30px;" + \
        "}"

        return css

    elif ("studentMsgSel" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 16px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:rgb(200,200,200);" + \
        "border:0px solid transparent;" + \
        "border-radius:0px;" + \
        "padding:10px;" + \
        "}" + \
        "QPushButton::hover {" + \
        "background-color:white;" + \
        "}" + \
        "QPushButton:checked {" + \
        "background-color: transparent;" + \
        "border: 2px solid black; }"

        return css


    elif ("studentName" == widget):

        css = \
        "QLineEdit {" + \
        "font-size: 20px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:rgb(190,190,190);" + \
        "border:3px solid transparent;" + \
        "border-radius:0px;" + \
        "padding:5px;" + \
        "}"

        return css


    elif ("studentNameLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size: 20px; font-weight:bold;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "}"

        return css

    elif ("convoText" == widget):

        css = \
        "QTextEdit {" + \
        "font-size: 14px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border-top:1px solid rgb(200,200,200);" + \
        "border-left:1px solid rgb(200,200,200);" + \
        "border-radius:0px;" + \
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
