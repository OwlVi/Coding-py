#time def
#input
def read_hour():
    h = int(input("Enter hour: "))
    return h
def read_minute():
    m = int(input("Enter minute: "))
    return m
def read_second():
    s = int(input("Enter second: "))
    return s
#process

def to_seconds(h, m, s):
    sumtime = (h*60*60)+(m*60)+s
    return sumtime

def time_elapsed(start, finish):
    t = finish - start
    h = (t//(60*60))
    m = (t%(60*60))//60
    s = (t%60)
    time = f"{h} hours {m} minutes {s} seconds."
    return time

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)
#output
print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))