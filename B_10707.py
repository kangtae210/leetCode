import sys

x_plus = int(sys.stdin.readline())      # X사 리터당 요금
y_base = int(sys.stdin.readline())      # Y사 기본요금
y_check = int(sys.stdin.readline())     # Y사 추가요금 기준선
y_plus = int(sys.stdin.readline())      # Y사 리터당 추가요금
use = int(sys.stdin.readline())         # 한달간 사용하는 수도의 양

y_money = y_base + max(0, use - y_check) * y_plus
x_money = x_plus * use

print(min(y_money, x_money))