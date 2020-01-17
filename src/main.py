#!/usr/local/bin/python3.6
import com,timer,gui
import UI as ui



def run():
    gui_connect()


def gui_connect():
    # handles the connection with the gui lib
    app = gui.QtWidgets.QApplication(gui.sys.argv)
    ex = gui.App()
    gui.sys.exit(app.exec())

def ui_connect():
    login_info = ui.get_login()
    library = ui.get_library()
    room = ui.get_room()
    date = ui.get_date()
    time = ui.get_time()
    addr = ui.get_addr(library, room, date, time)
    #timer.timer(time,True)
    c = com.communication()
    print(addr)
    #timer.timer(time, True)
    c.login(email=login_info[0], password=login_info[1], addr=addr)
    c.book() # removed addr
    c.quit()

if __name__ == "__main__":
    run()
