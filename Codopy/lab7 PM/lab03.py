#hheelllloo monday
#input
d_ay  = int(input())
h_our = int(input())
m_in  = int(input())

#process
if d_ay == 1 :
    day = 'sunday'
elif d_ay == 2 :
    day = 'monday'    
elif d_ay == 3 :
    day = 'tuesday'
elif d_ay == 4 :
    day = 'wednesday'
elif d_ay == 5 :
    day = 'thursday'
elif d_ay == 6 :
    day = 'friday'
elif d_ay == 7 :
    day = 'saturday'    
#time 
if   ( 4 <= h_our < 12 and  0 < m_in ) or ( h_our == 12 and m_in == 0 ):
    time = 'morning'
elif ( 12 <= h_our < 18 and 0 < m_in ) or ( h_our == 18 and m_in == 0 ):
    time = 'afternoon'
elif ( 18 <= h_our < 22 and 0 < m_in ) or ( h_our == 22 and m_in == 0 ):
    time = 'evening'
else:
    time = 'night' 
    
#output
print(f'good-{time}-{day}.png')
