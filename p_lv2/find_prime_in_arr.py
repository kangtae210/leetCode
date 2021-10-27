from itertools import permutations

def is_prime_num(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(pow(n, 0.5))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True

def solution(numbers):
    count = 0
    answer = []
    for i in range(len(numbers)):
        x = list(permutations(numbers, i+1))
        for j in range(len(x)):
            answer.append(int("".join(list(x[j]))))
    answer = list(set(answer))
    
    for one in answer:
        if is_prime_num(one):
            print(one)
            count += 1



    return count


print(solution("17"))     # 3
print()
print(solution("011"))    # 2












