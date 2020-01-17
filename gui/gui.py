
# TODO time range
import sys,bookme, com, timer,UI as ui
from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore

shift = 10

class App(QtWidgets.QWidget):

    # Constructor
    def __init__(self):
        super().__init__()

        self.title = 'BookMe-BOT'
        self.height =600
        self.width =700
        self.initUI()


    def initUI(self):
        self.state = False
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowTitle(self.title)
        self.main_layout()
        self.setFixedSize(self.width, self.height)
        self.show()

    # Returns the date as string in 'ddmm' format
    def format_date(self,date):
        months = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05'
                ,'Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10'
                ,'Nov':'11','Dec':'12'}
        date = str(date).split('/')
        return date[0]+months.get(date[1])

    # Returns the time as a tuple with two formatted strings
    def format_time(self,start,end):
        return [str(start)[0:2]+str(start)[3:5],str(end)[0:2]+str(end)[3:5]]

    # Returns the given room url code
    def get_room(self,room):
        return bookme.rooms.get(room)

    # for now returns only the url code for fishbach
    def get_library(self):
        return bookme.library.get('fishbach')

    #Makes sure that the time is in half hours format
    def fix_time(self):
        self.time = (self.format_time(self.time_start.text(), self.time_end.text()))
        for i in range(0,2):
            if int(self.time[i][2]) > 3:
                self.time[i] = self.time[i][0:2]+'30'
            else:
                self.time[i] =self.time[i][0:2]+'00'

    #Checks if the time is valid
    def check_time(self):
        if int(self.time[0])>= int(self.time[1]):
            return False
        for i in range(0,2):
            if int(self.time[i][0:2])< 8 or int(self.time[i][0:2]) > 19:
                return False
        return True

    #Checks if the email id valid
    def check_email(self):
        if self.l_email.text().__contains__('@campus.technion.ac.il'):
            return True
        return False

    # def check_date(self): TODO check date function

    #Checks if the password is valid
    def check_password(self):
        if len(self.l_password.text())<8:
            return False
        return True

    #Runs the checklist
    def check_list(self):
        if not self.check_email():
            self.t_errors.setText('Invalid Email!')
            return False
        if not self.check_time():
            self.t_errors.setText('Invalid Time!')
            return False
        if not self.check_password():
            self.t_errors.setText('Invalid Password!')
            return False

        return True


    def pre_run(self):
        self.t_errors.clear()
        self.fix_time()
        if self.check_list():
            self.run()


    def run(self):
        self.email = self.l_email.text()
        self.password = self.l_password.text()
        self.room = self.rooms.currentText()
        self.choosen_date = self.date.text()

        self.l_email.clear()
        self.l_password.clear()
        library = self.get_library()
        room =self.get_room(self.room)
        addr = bookme.get_addr(library,room, bookme.date_format(self.format_date(self.choosen_date)), self.time)
        print(self.time)
        # self.t_errors.setText("Request Will be sended at: "+self.time[0])
        timer.timer(self.time[0],pre_timer=True)
        print("[*]Passed First Timer") # Debug
        c = com.communication()
        c.login(email=self.email, password=self.password, addr=addr)
        self.t_errors.setText("Login Request has sended.")
        timer.timer(self.time[0],pre_timer=False)
        print("[*]Passed second Timer") # Debug
        c.book(addr=addr)
        self.t_errors.setText("Booking Request has sended.")
        c.quit()




    def main_layout(self):

        #Group Box:

        g_box_login = QtWidgets.QGroupBox()
        g_box_login.setTitle("Login Info")

        g_box_data = QtWidgets.QGroupBox()

        # labels:
        t_email= QtWidgets.QLabel('  Email:')
        t_password = QtWidgets.QLabel('  Password:')
        t_room = QtWidgets.QLabel('  Room:')
        t_date = QtWidgets.QLabel('  Date:')
        t_start =QtWidgets.QLabel('  Start:')
        t_end = QtWidgets.QLabel('  End: ')
        self.t_errors = QtWidgets.QLabel()

        # text edits:
        self.l_email = QtWidgets.QLineEdit()
        self.l_password = QtWidgets.QLineEdit()
        self.l_password.setEchoMode(QtWidgets.QLineEdit.Password)



        # Combo Box:
        self.rooms = QtWidgets.QComboBox()
        self.rooms.setObjectName("Room")
        self.rooms.addItems(bookme.rooms)

        # Date:
        self.date = QtWidgets.QDateEdit()
        self.date.setDate(QtCore.QDate.currentDate())
        self.date.setDisplayFormat('dd/MMM')

        # Time:
        self.time_start = QtWidgets.QTimeEdit()
        self.time_start.setTime(QtCore.QTime.currentTime())
        self.time_start.setDisplayFormat('hh:mm')


        self.time_end = QtWidgets.QTimeEdit()
        self.time_end.setTime(QtCore.QTime.currentTime())

        # Button:

        btn_submit = QtWidgets.QPushButton('Submit',self)
        btn_submit.clicked.connect(self.pre_run)


        # grid managment:
        grid = QtWidgets.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(g_box_login,0,0,5,6)

        grid.addWidget(g_box_data, 6, 0, 5, 6)

        grid.addWidget(t_email,1,0)
        grid.addWidget(self.l_email,1,1,1,4)

        grid.addWidget(t_password, 2, 0)
        grid.addWidget(self.l_password, 2, 1,1,4)


        grid.addWidget(t_date, 7, 0)
        grid.addWidget(self.date, 7, 1)

        grid.addWidget(t_start,8,0)
        grid.addWidget(self.time_start,8,1)

        grid.addWidget(t_end, 7, 2)
        grid.addWidget(self.time_end, 7, 3)

        grid.addWidget(t_room,8,2)
        grid.addWidget(self.rooms,8,3)

        grid.addWidget(btn_submit,11,0,7,6)

        grid.addWidget(self.t_errors,3,1,1,3)
        self.setLayout(grid)
