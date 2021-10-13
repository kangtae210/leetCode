# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 
# solution 함수를 완성해주세요.

def solution2(n):
    target = ""
    while n !=0:
        target += str(n % 3)
        n = n //3

    digit = len(target)
    for i in range(digit):
        n += int(target[i]) * (3 ** (digit - i-1))

    return n


def solution(n):
    answer = 0
    digits = 0
    while n > 0 :
        answer = answer * 3 + (n%3)
        n = n // 3
        digits += 1
    return answer
      


case = solution(45)
print(case)     # 7

case = solution(125)
print(case)     # 229