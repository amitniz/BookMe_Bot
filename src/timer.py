import datetime
date = datetime.datetime.now()


def get_year():

    return date.now().year

def delay():
    time = str(datetime.datetime.now().time())[6:8]
    new_time = str(datetime.datetime.now().time())[6:8]
    while(int(new_time)<(int(time)+2)):
        new_time = str(datetime.datetime.now().time())[6:8]
    print(new_time) #debug

# Loops until the time for the request
def timer(call_time,pre_timer):
    time = str(datetime.datetime.now().time())
    time = str(time)[0:2]+str(time)[3:5]

    if pre_timer:

        while (int(call_time)+1 > int(time)):

            time = str(datetime.datetime.now().time())
            time = str(time)[0:2] + str(time)[3:5]

        print("[*]Login Request has sended.")
    else:

        while (int(call_time)>int(time[0])):

            time = str(datetime.datetime.now().time())
            time = [time[i:i + 2] for i in range(0, len(time), 3)]

        print("[*]Booking Request has sended.")
