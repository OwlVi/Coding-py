# time def

def read_hour():
    h = int(input("Enter hour: "))
    return h
def read_minute():
    m = int(input("Enter minute: "))
    return m
def read_second():
    s = int(input("Enter second: "))
    return s

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)
def to_seconds(h, m, s):
    sumtime = (h*60*60)+(m*60)+s
    return sumtime

def time_elapsed(start, finish):
    finish -= start
    h = (finish//60//24)
    m = (finish//60)
    s = (finish%60)
    time = f"{h} hours {m} minutes {s} seconds."
    return time

#input 

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))