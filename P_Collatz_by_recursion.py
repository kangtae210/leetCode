# 콜라츠 추측을 재귀함수를 이용해 수행하는 방법
def is_collatz(num):
    print(num, "→ ", end="")
    if num == 1:
        print('True')
    elif num % 2 == 0:
        is_collatz(int(num / 2))
    else:
        is_collatz(3* num + 1)

x = is_collatz(123)
    