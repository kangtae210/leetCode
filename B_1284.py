import sys

def cal_width(address):
    width = 0
    for i in address:
        i = int(i)
        if i == 0:
            width += 4
        elif i == 1:
            width += 2
        else:
            width += 3
    return width +len(address) + 1


cases = []
while True:
    input_str = input()
    if input_str == '0':
        break
    cases.append(cal_width(input_str))

for i in cases:
    print(i)