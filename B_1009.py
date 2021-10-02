import sys


testCase = int(sys.stdin.readline())
answers = []
for i in range(testCase):
    x,y = map(int, sys.stdin.readline().split())
    num = int(pow(x,y,10))
    if num == 0:
        num = 10
    answers.append(num)

for i in answers:
    print(i)
    




