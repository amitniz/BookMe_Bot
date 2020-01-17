import timer

rooms = {'463': '107','464': '26','468': '27','469': '28','470': '29'
        ,'471': '30','472': '31','475': '32','476': '33','477': '34'
        ,'478': '35','480': '36','481': '39','482': '37','483': '38'}

library = {'fishbach': '8'}

def time_format(time):
    splited_time = split2(time)
    formated_time =['20'+splited_time[0],'3A'+splited_time[1]]
    return formated_time
# Returns the requested url as BookMe url format
def build_addr(library,room,date,from_time,to_time):
    return 'https://bookme.technion.ac.il/booked/Web/reservation.php?rid='+room+'&sid='+library+'&rd='+date+ \
           '&sd='+date+'%'+from_time[0]+'%'+from_time[1]+'%3A00&ed='+date+'%'+to_time[0]+'%'+to_time[1]+'%3A00'
# Returns the date in BookMe format
def date_format(date):
    split = split2(date)
    return str(timer.get_year()) + "-" + split[1] + "-" + split[0]


def split2(n):
    return [n[i:i + 2] for i in range(0, len(n), 2)]

# Same as build_addr, just separetes the time. don't remember why I did that, I guess I had a reason..
def get_addr(library,room,date,time):
    time =[time_format(time[0]),time_format(time[1])]
    addr= build_addr(library,room,date,time[0],time[1])
    print(addr)
    return addr
