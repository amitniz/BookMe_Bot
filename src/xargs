

import bookme,getpass


def get_date():
    date = input("[+]Please Insert the date: (ddmm)\n")
    if check_date(date):
        return bookme.date_format(date)
    else:
        print("[!]Wrong date")
        return get_date()

def check_date(date):
    if len(date) != 4:
        return False
    split = bookme.split2(date)
    if (int(split[0]) > 31 or int(split[0]) < 1) or (int(split[1]) > 12 or int(split[1]) < 1):
        return False
    return True

def get_time():
    fm=input("From: ")
    to=input("Until: ")
    if check_time(fm,to):
        return [fm,to]
    else:
        print('[!]Wrong Time try again (hhmm)')
        return get_time()

def check_time(fm,to):
    if len(fm) != 4 or len(to) != 4 or fm >= to:
        return False

    fm = bookme.split2(fm)
    to = bookme.split2(to)
    if int(fm[0])>23 or int(to[0])>23 or int(fm[0])<8 or int(to[0])<8:
        return False
    elif (int(fm[1]) != 0 and int(fm[1]) != 30) or (int(to[1]) != 0 and int(to[1]) != 30):
        return False
    return True

def get_login():
    email = input("Email: ")
    password = getpass.getpass("Password: ")
    return [email,password]

def get_library():
    return bookme.library.get('fishbach')

def get_room(room):
    if room in bookme.rooms.keys():
        return bookme.rooms.get(room)
    print("[!]Wrong Room:")
    return get_room()

