# StyleSheet class returns CSS stylesheets for QWidgets

class StyleSheet(object):

  msgHTML         = "<p style=\" margin:5px; \" >"
  timestampHTML   = "<span style=\" font-size:12px; font-style:italic; \" >"
  studentNameHTML = "<span style=\" color:#0000FF; \" >"
  teacherNameHTML = "<span style=\" color:#BB00FF; \" >"

  def __init__(self, arg):
    super(StyleSheet, self).__init__()
    self.arg = arg
    
  def css(widget=None):

    if ("window" == widget):

        css = \
        "QWidget {" + \
        "font-family:Montserrat;" + \
        "color:rgb(255,255,255);" + \
        "background-color:rgb(230,230,230);" + \
        "}" + \
        "QScrollBar:vertical {" + \
        "background:rgb(200,200,200);" + \
        "width:10px;" + \
        "border:0px;" + \
        "margin: 0px 0px 0px 0px;" + \
        "}"

        return css

    elif ("button" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 14px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:1px solid black;" + \
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
        "color:black;" + \
        "background-color:rgb(200,200,200);" + \
        "border-radius:0px;" + \
        "}"

        return css

    elif ("clock" == widget):

        css = \
        "QLabel {" + \
        "font-size:30px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "}"
        
        return css

    elif ("hours" == widget):

        css = \
        "QLabel {" + \
        "font-size:28px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "}"

        return css

    elif ("hoursLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size:24px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "}"

        return css

    elif ("available" == widget):

        css = \
        "QLabel {" + \
        "font-size:20px;" + \
        "color:black;" + \
        "background-color:rgb(150,255,150);" + \
        "border: 1px solid black;" + \
        "border-radius:20px;" + \
        "}"

        return css

    elif ("unavailable" == widget):

        css = \
        "QLabel {" + \
        "font-size:20px;" + \
        "color:black;" + \
        "background-color:rgb(255,150,150);" + \
        "border: 1px solid black;" + \
        "border-radius:20px;" + \
        "}"

        return css

    elif ("msgGroupBox" == widget):

        css = \
        "QGroupBox {" + \
        "font-size: 28px;" + \
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
        "font-size: 16px;" + \
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

    elif ("sendMsgBtn" == widget):

        css = \
        "QPushButton {" + \
        "font-size: 20px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:1px solid black;" + \
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

    elif ("studentName" == widget):

        css = \
        "QLineEdit {" + \
        "font-size: 20px;" + \
        "color:black;" + \
        "background-color:rgb(200,200,200);" + \
        "border:3px solid transparent;" + \
        "border-radius:0px;" + \
        "padding:5px;" + \
        "}"

        return css


    elif ("studentNameLabel" == widget):

        css = \
        "QLabel {" + \
        "font-size: 20px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border:3px solid transparent;" + \
        "border-radius:10px;" + \
        "}"

        return css

    elif ("convoText" == widget):

        css = \
        "QTextEdit {" + \
        "font-size: 13px;" + \
        "color:black;" + \
        "background-color:transparent;" + \
        "border-top:1px solid rgb(200,200,200);" + \
        "border-left:1px solid rgb(200,200,200);" + \
        "border-radius:0px;" + \
        "margin-right:0px;" + \
        "}"

        return css

    elif ("status" == widget):

        css = \
        "QStatusBar {" + \
        "font-family:Montserrat;" + \
        "color:black;" + \
        "background-color:rgb(200,200,200);" + \
        "}"

        return css

    elif ("spacer" == widget):

        css = \
        "QLabel {" + \
        "background-color:transparent;" + \
        "}"

        return css
