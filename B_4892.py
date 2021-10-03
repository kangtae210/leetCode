import sys
import math

i = 1
while True:
    index = str(i) + "."
    number = int(sys.stdin.readline())  #n0
    if number == 0:
        break
   
    number = number * 3                 #n1 = 3n0
    x = ''
    if number % 2 == 0:
        x = 'even'
    else:
        x = 'odd'
    if number % 2 == 0:                  #n2 = n1/2 or (n1+1) / 2
        number = number / 2                
    else:
        number = (number+1) / 2
    number = number * 3                 #n3
    y = math.floor(number / 9 )

    print(index,x, y)
    i += 1
    