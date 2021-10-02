import sys
import math

musics, avg = map(int, sys.stdin.readline().split())
answer = musics * avg

while True:
    answer = answer -1
    if math.ceil(answer / musics) != avg:
         answer = answer + 1
         break

print(answer)
