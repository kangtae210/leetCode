import sys
a = int(sys.stdin.readline()) % 8

if a == 1:
    a = 1
if a == 2:
    a = 2
if a == 3:
    a = 3
if a == 4:
    a = 4
if a == 5:
    a = 5
if a == 6:
    a = 4
if a == 7:
    a = 3
if a == 0:
    a = 2

print(a)
