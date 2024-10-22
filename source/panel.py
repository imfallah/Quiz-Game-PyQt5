
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_quiz(object):
    def setupUi(self, quiz):
        quiz.setObjectName("quiz")

        quiz.resize(1071,700)

        self.centralwidget = QtWidgets.QWidget(quiz)
        self.centralwidget.setObjectName("centralwidget")
        self.pages = QtWidgets.QStackedWidget(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.pages.setObjectName("pages")
        self.start = QtWidgets.QWidget()
        self.start.setStyleSheet("border-radius: 1px;")
        self.start.setObjectName("start")
        self.back_start = QtWidgets.QLabel(self.start)
        self.back_start.setGeometry(QtCore.QRect(0, -10, 1081, 731))
        self.back_start.setText("")
        self.back_start.setPixmap(QtGui.QPixmap("../images/2.jpg"))
        self.back_start.setObjectName("back_start")
        self.gametolearn = QtWidgets.QLabel(self.start)
        self.gametolearn.setGeometry(QtCore.QRect(360, 200, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        self.gametolearn.setFont(font)
        self.gametolearn.setStyleSheet("color: rgb(255, 255, 255);")
        self.gametolearn.setAlignment(QtCore.Qt.AlignCenter)
        self.gametolearn.setObjectName("gametolearn")
        self.letsgo = QtWidgets.QPushButton(self.start)
        self.letsgo.setGeometry(QtCore.QRect(429, 467, 351, 81))
        font = QtGui.QFont()
        font.setFamily("Kalameh Black")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.letsgo.setFont(font)
        self.letsgo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.letsgo.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    color: rgb(55, 26, 70);\n"
"}")
        self.letsgo.setObjectName("letsgo")
        self.label = QtWidgets.QLabel(self.start)
        self.label.setGeometry(QtCore.QRect(0, 250, 731, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/logo.png"))
        self.label.setObjectName("label")
        self.pages.addWidget(self.start)
        self.select = QtWidgets.QWidget()
        self.select.setStyleSheet("border-radius: 1px;")
        self.select.setObjectName("select")
        self.back_select = QtWidgets.QLabel(self.select)
        self.back_select.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.back_select.setText("")
        ##
        self.back_select.setPixmap(QtGui.QPixmap("../images/3.jpg"))
        self.back_select.setObjectName("back_select")
        self.title_select = QtWidgets.QLabel(self.select)
        self.title_select.setGeometry(QtCore.QRect(0, 110, 1081, 81))
        font = QtGui.QFont()
        font.setFamily("Kalameh Black")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.title_select.setFont(font)
        self.title_select.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_select.setAlignment(QtCore.Qt.AlignCenter)
        self.title_select.setObjectName("title_select")
        self.tech = QtWidgets.QPushButton(self.select)
        self.tech.setGeometry(QtCore.QRect(710, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.tech.setFont(font)
        self.tech.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tech.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.tech.setObjectName("tech")
        self.sport = QtWidgets.QPushButton(self.select)
        self.sport.setGeometry(QtCore.QRect(430, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.sport.setFont(font)
        self.sport.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sport.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.sport.setObjectName("sport")
        self.info = QtWidgets.QPushButton(self.select)
        self.info.setGeometry(QtCore.QRect(140, 220, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.info.setFont(font)
        self.info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.info.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.info.setObjectName("info")
        self.cinema = QtWidgets.QPushButton(self.select)
        self.cinema.setGeometry(QtCore.QRect(710, 330, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.cinema.setFont(font)
        self.cinema.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cinema.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.cinema.setObjectName("cinema")
        self.math = QtWidgets.QPushButton(self.select)
        self.math.setGeometry(QtCore.QRect(140, 330, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.math.setFont(font)
        self.math.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.math.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.math.setObjectName("math")
        self.nature = QtWidgets.QPushButton(self.select)
        self.nature.setGeometry(QtCore.QRect(430, 330, 231, 61))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.nature.setFont(font)
        self.nature.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nature.setStyleSheet("QPushButton {\n"
"    background-color: rgb(196, 93, 255);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(95, 0, 143);\n"
"    color: rgb(181, 83, 255);\n"
"}")
        self.nature.setObjectName("nature")
        self.label_3 = QtWidgets.QLabel(self.select)
        self.label_3.setGeometry(QtCore.QRect(330, 380, 381, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../images/Astronautـselect.png"))
        self.label_3.setObjectName("label_3")
        self.level = QtWidgets.QLabel(self.select)
        self.level.setGeometry(QtCore.QRect(100, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Street - Plain")
        font.setPointSize(16)
        font.setItalic(False)
        self.level.setFont(font)
        self.level.setStyleSheet("color: rgb(249, 249, 249);")
        self.level.setObjectName("level")
        self.username = QtWidgets.QLabel(self.select)
        self.username.setGeometry(QtCore.QRect(100, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cocogoose [pyrs]")
        font.setPointSize(14)
        font.setItalic(False)
        self.username.setFont(font)
        self.username.setStyleSheet("color: rgb(249, 249, 249);")
        self.username.setObjectName("username")
        self.profile = QtWidgets.QLabel(self.select)
        self.profile.setGeometry(QtCore.QRect(30, 20, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Cocogoose [pyrs]")
        font.setPointSize(16)
        font.setItalic(False)
        self.profile.setFont(font)
        self.profile.setStyleSheet("background-color: rgb(226, 178, 255, 200);\n"
"border-radius: 25px;\n"
"color: rgb(44, 18, 66);")
        self.profile.setAlignment(QtCore.Qt.AlignCenter)
        self.profile.setObjectName("profile")
        self.pages.addWidget(self.select)
        self.question = QtWidgets.QWidget()
        self.question.setObjectName("question")
        self.back_question = QtWidgets.QLabel(self.question)
        self.back_question.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.back_question.setText("")
        self.back_question.setPixmap(QtGui.QPixmap("../images/4copy.jpg"))
        self.back_question.setObjectName("back_question")
        self.frame = QtWidgets.QFrame(self.question)
        self.frame.setGeometry(QtCore.QRect(240, 110, 631, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.quest = QtWidgets.QLabel(self.frame)
        self.quest.setGeometry(QtCore.QRect(0, 30, 611, 51))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.quest.setFont(font)
        self.quest.setStyleSheet("color: rgb(43, 41, 104);")
        self.quest.setText("")
        self.quest.setAlignment(QtCore.Qt.AlignCenter)
        self.quest.setObjectName("quest")
        self.one = QtWidgets.QPushButton(self.frame)
        self.one.setGeometry(QtCore.QRect(330, 130, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.one.setFont(font)
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.one.setText("")
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.frame)
        self.two.setGeometry(QtCore.QRect(60, 130, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.two.setFont(font)
        self.two.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.two.setText("")
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.frame)
        self.three.setGeometry(QtCore.QRect(330, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.three.setFont(font)
        self.three.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.three.setText("")
        self.three.setObjectName("three")
        self.four = QtWidgets.QPushButton(self.frame)
        self.four.setGeometry(QtCore.QRect(60, 210, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.four.setFont(font)
        self.four.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.four.setText("")
        self.four.setObjectName("four")
        self.time = QtWidgets.QLabel(self.frame)
        self.time.setGeometry(QtCore.QRect(270, 280, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(24)
        self.time.setFont(font)
        self.time.setStyleSheet("color: rgb(43, 41, 104);")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.time.setObjectName("time")
        self.line2 = QtWidgets.QLabel(self.frame)
        self.line2.setGeometry(QtCore.QRect(60, 150, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.line2.setFont(font)
        self.line2.setStyleSheet("background-color: none;\n"
"color: rgb(85, 85, 127);")
        self.line2.setObjectName("line2")
        self.line1 = QtWidgets.QLabel(self.frame)
        self.line1.setGeometry(QtCore.QRect(330, 150, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.line1.setFont(font)
        self.line1.setStyleSheet("background-color: none;\n"
"color: rgb(85, 85, 127);")
        self.line1.setObjectName("line1")
        self.line3 = QtWidgets.QLabel(self.frame)
        self.line3.setGeometry(QtCore.QRect(330, 230, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.line3.setFont(font)
        self.line3.setStyleSheet("background-color: none;\n"
"color: rgb(85, 85, 127);")
        self.line3.setObjectName("line3")
        self.line4 = QtWidgets.QLabel(self.frame)
        self.line4.setGeometry(QtCore.QRect(60, 230, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.line4.setFont(font)
        self.line4.setStyleSheet("background-color: none;\n"
"color: rgb(85, 85, 127);")
        self.line4.setObjectName("line4")
        self.quest_2 = QtWidgets.QLabel(self.frame)
        self.quest_2.setGeometry(QtCore.QRect(10, 70, 611, 51))
        font = QtGui.QFont()
        font.setFamily("IRANSans")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.quest_2.setFont(font)
        self.quest_2.setStyleSheet("color: rgb(43, 41, 104);")
        self.quest_2.setText("")
        self.quest_2.setAlignment(QtCore.Qt.AlignCenter)
        self.quest_2.setObjectName("quest_2")
        self.one.raise_()
        self.two.raise_()
        self.three.raise_()
        self.four.raise_()
        self.time.raise_()
        self.line2.raise_()
        self.line1.raise_()
        self.line3.raise_()
        self.line4.raise_()
        self.quest_2.raise_()
        self.quest.raise_()
        self.frame_4 = QtWidgets.QFrame(self.question)
        self.frame_4.setGeometry(QtCore.QRect(650, 659, 421, 51))
        self.frame_4.setStyleSheet("background-color: rgba(255, 255, 255, 170);\n"
"border-radius: 8px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.buy_time = QtWidgets.QPushButton(self.frame_4)
        self.buy_time.setGeometry(QtCore.QRect(230, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(18)
        self.buy_time.setFont(font)
        self.buy_time.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buy_time.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    color: rgb(43, 41, 104);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: none;\n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.buy_time.setIconSize(QtCore.QSize(26, 33))
        self.buy_time.setObjectName("buy_time")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 7, 51, 41))
        self.pushButton_2.setStyleSheet("background-color: none;")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/time-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(35, 35))
        self.pushButton_2.setObjectName("pushButton_2")
        self.buy_option = QtWidgets.QPushButton(self.frame_4)
        self.buy_option.setGeometry(QtCore.QRect(0, 0, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(18)
        self.buy_option.setFont(font)
        self.buy_option.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buy_option.setStyleSheet("QPushButton {\n"
"    background-color: none;\n"
"    color: rgb(43, 41, 104);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: none;\n"
"    color: rgb(0, 0, 127);\n"
"}")
        self.buy_option.setIconSize(QtCore.QSize(26, 33))
        self.buy_option.setObjectName("buy_option")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_4.setGeometry(QtCore.QRect(160, 0, 41, 51))
        self.pushButton_4.setStyleSheet("background-color: none;")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../images/delete-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.raise_()
        self.pushButton_2.raise_()
        self.buy_time.raise_()
        self.buy_option.raise_()
        self.frame_5 = QtWidgets.QFrame(self.question)
        self.frame_5.setGeometry(QtCore.QRect(10, 660, 421, 51))
        self.frame_5.setStyleSheet("background-color: rgba(255, 255, 255, 150);\n"
"border-radius: 8px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_coin = QtWidgets.QLabel(self.frame_5)
        self.label_coin.setGeometry(QtCore.QRect(67, 0, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(18)
        self.label_coin.setFont(font)
        self.label_coin.setStyleSheet("background-color: none;\n"
"color: rgb(43, 41, 104);")
        self.label_coin.setObjectName("label_coin")
        self.level2 = QtWidgets.QLabel(self.frame_5)
        self.level2.setGeometry(QtCore.QRect(20, 0, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(18)
        self.level2.setFont(font)
        self.level2.setStyleSheet("background-color: none;\n"
"color: rgb(43, 41, 104);")
        self.level2.setAlignment(QtCore.Qt.AlignCenter)
        self.level2.setObjectName("level2")
        self.label_user = QtWidgets.QLabel(self.frame_5)
        self.label_user.setGeometry(QtCore.QRect(280, 0, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(18)
        self.label_user.setFont(font)
        self.label_user.setStyleSheet("background-color: none;\n"
"color: rgb(43, 41, 104);")
        self.label_user.setObjectName("label_user")
        self.username2 = QtWidgets.QLabel(self.frame_5)
        self.username2.setGeometry(QtCore.QRect(233, 0, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        self.username2.setFont(font)
        self.username2.setStyleSheet("background-color: none;\n"
"color: rgb(43, 41, 104);")
        self.username2.setAlignment(QtCore.Qt.AlignCenter)
        self.username2.setObjectName("username2")
        self.pages.addWidget(self.question)
        self.True_answer = QtWidgets.QWidget()
        self.True_answer.setObjectName("True_answer")
        self.back_win = QtWidgets.QLabel(self.True_answer)
        self.back_win.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.back_win.setText("")
        self.back_win.setPixmap(QtGui.QPixmap("../images/4.jpg"))
        self.back_win.setObjectName("back_win")
        self.frame_2 = QtWidgets.QFrame(self.True_answer)
        self.frame_2.setGeometry(QtCore.QRect(280, 80, 511, 311))
        self.frame_2.setStyleSheet("background-color: rgba(255, 255, 255,);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.title_win = QtWidgets.QLabel(self.frame_2)
        self.title_win.setGeometry(QtCore.QRect(40, 10, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Kalameh Black")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.title_win.setFont(font)
        self.title_win.setStyleSheet("color: rgb(66, 27, 92);\n"
"transform: rotate(30deg);\n"
"background-color: none;")
        self.title_win.setAlignment(QtCore.Qt.AlignCenter)
        self.title_win.setObjectName("title_win")
        self.next = QtWidgets.QPushButton(self.frame_2)
        self.next.setGeometry(QtCore.QRect(280, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.next.setFont(font)
        self.next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.next.setObjectName("next")
        self.end = QtWidgets.QPushButton(self.frame_2)
        self.end.setGeometry(QtCore.QRect(80, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.end.setFont(font)
        self.end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.end.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.end.setObjectName("end")
        self.quest_win = QtWidgets.QLabel(self.frame_2)
        self.quest_win.setGeometry(QtCore.QRect(0, 110, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.quest_win.setFont(font)
        self.quest_win.setStyleSheet("background-color: none;\n"
"color: rgb(0, 0, 0);")
        self.quest_win.setText("")
        self.quest_win.setAlignment(QtCore.Qt.AlignCenter)
        self.quest_win.setObjectName("quest_win")
        self.answer_win = QtWidgets.QLabel(self.frame_2)
        self.answer_win.setGeometry(QtCore.QRect(0, 160, 511, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.answer_win.setFont(font)
        self.answer_win.setStyleSheet("background-color: none;\n"
"color: rgb(234, 54, 128);")
        self.answer_win.setText("")
        self.answer_win.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_win.setObjectName("answer_win")
        self.pages.addWidget(self.True_answer)
        self.False_answer = QtWidgets.QWidget()
        self.False_answer.setObjectName("False_answer")
        self.back_lost = QtWidgets.QLabel(self.False_answer)
        self.back_lost.setGeometry(QtCore.QRect(0, 0, 1081, 721))
        self.back_lost.setText("")
        self.back_lost.setPixmap(QtGui.QPixmap("../images/3.jpg"))
        self.back_lost.setObjectName("back_lost")
        self.frame_3 = QtWidgets.QFrame(self.False_answer)
        self.frame_3.setGeometry(QtCore.QRect(280, 80, 521, 311))
        self.frame_3.setStyleSheet("background-color: rgba(255, 255, 255,);\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.title_lost = QtWidgets.QLabel(self.frame_3)
        self.title_lost.setGeometry(QtCore.QRect(40, 10, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Kalameh Black")
        font.setPointSize(42)
        font.setBold(True)
        font.setWeight(75)
        self.title_lost.setFont(font)
        self.title_lost.setStyleSheet("color: rgb(66, 27, 92);\n"
"transform: rotate(30deg);\n"
"background-color: none;")
        self.title_lost.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lost.setObjectName("title_lost")
        self.next2 = QtWidgets.QPushButton(self.frame_3)
        self.next2.setGeometry(QtCore.QRect(280, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.next2.setFont(font)
        self.next2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.next2.setObjectName("next2")
        self.end2 = QtWidgets.QPushButton(self.frame_3)
        self.end2.setGeometry(QtCore.QRect(80, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.end2.setFont(font)
        self.end2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.end2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(238, 87, 138, 150);\n"
"    border-radius: 20px;\n"
"    color: rgb(31, 12, 47);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(238, 87, 138, 250);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.end2.setObjectName("end2")
        self.quest_lost = QtWidgets.QLabel(self.frame_3)
        self.quest_lost.setGeometry(QtCore.QRect(0, 110, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.quest_lost.setFont(font)
        self.quest_lost.setStyleSheet("background-color: none;\n"
"color: rgb(0, 0, 0);")
        self.quest_lost.setText("")
        self.quest_lost.setAlignment(QtCore.Qt.AlignCenter)
        self.quest_lost.setObjectName("quest_lost")
        self.answer_lost = QtWidgets.QLabel(self.frame_3)
        self.answer_lost.setGeometry(QtCore.QRect(0, 160, 521, 41))
        font = QtGui.QFont()
        font.setFamily("Kalameh [    ]")
        font.setPointSize(22)
        self.answer_lost.setFont(font)
        self.answer_lost.setStyleSheet("background-color: none;\n"
"color: rgb(234, 54, 128);")
        self.answer_lost.setText("")
        self.answer_lost.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_lost.setObjectName("answer_lost")
        self.pages.addWidget(self.False_answer)
        quiz.setCentralWidget(self.centralwidget)

        self.retranslateUi(quiz)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(quiz)

    def retranslateUi(self, quiz):
        _translate = QtCore.QCoreApplication.translate
        quiz.setWindowTitle(_translate("quiz", "MainWindow"))
   #     self.gametolearn.setText(_translate("quiz", "بازی کن و یادبگیر"))
        self.letsgo.setText(_translate("quiz", "Lets Go"))
        self.title_select.setText(_translate("quiz", "Please select the question category"))
        self.tech.setText(_translate("quiz", "Technology"))
        self.sport.setText(_translate("quiz", "Sports"))
        self.info.setText(_translate("quiz", "information"))
        self.cinema.setText(_translate("quiz", "the cinema"))
        self.math.setText(_translate("quiz", "Mathematics"))
        self.nature.setText(_translate("quiz", "Nature"))
        self.level.setText(_translate("quiz", "22"))
        self.username.setText(_translate("quiz", "user name"))
        self.profile.setText(_translate("quiz", "u"))
        self.time.setText(_translate("quiz", "00:08"))
        self.line2.setText(_translate("quiz", "--------------------------------"))
        self.line1.setText(_translate("quiz", "--------------------------------"))
        self.line3.setText(_translate("quiz", "--------------------------------"))
        self.line4.setText(_translate("quiz", "--------------------------------"))
        self.buy_time.setText(_translate("quiz", "Buy overtime      "))
        self.buy_option.setText(_translate("quiz", "Delete option "))
        self.label_coin.setText(_translate("quiz","Number of coins:"))
        self.level2.setText(_translate("quiz", "22"))
        self.label_user.setText(_translate("quiz", "User name:"))
        self.username2.setText(_translate("quiz", "elliott"))
        self.title_win.setText(_translate("quiz", "Perfact "))
        self.next.setText(_translate("quiz", "Let's go next"))
        self.end.setText(_translate("quiz", "Finish game"))
        self.title_lost.setText(_translate("quiz", "this False"))
        self.next2.setText(_translate("quiz", "Let's go next"))
        self.end2.setText(_translate("quiz", "Finish game"))
