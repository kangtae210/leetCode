import sys

case = int(sys.stdin.readline())

for i in range(case):
    s_people = []       # 세준 병사 모음(각 원소는 병사의 power)
    b_people = []       # 세비 병사 모음(각 원소는 병사의 power)
    s_count, b_count = map(int, sys.stdin.readline().split())
    s_people = sys.stdin.readline().split()
    b_people = sys.stdin.readline().split()

    s_people.sort()
    b_people.sort()

    repeat = 0
    while True:
        if len(s_people) == 0:
            print('B')
            break
        elif len(b_people) == 0:
            print('S')
            break
        if s_people[0] < b_people[0]:
            del s_people[0]
        elif s_people[0] == b_people[0]:
            del b_people[0]

        if repeat >= s_count + b_count:
            print('C')
            break
        repeat += 1
