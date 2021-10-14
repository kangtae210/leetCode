from itertools import combinations

# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
# 소수가 되는 경우의 개수를 return

def is_prime_num(n):
    for i in range(2, int(pow(n, 0.5))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return -1

    return n

def solution(nums):
    primes = []
    case = list(combinations(nums, 3))
    
    for i in case:
        primes.append(is_prime_num(sum(i)))

    return len(primes) - primes.count(-1)


case = solution([1, 2, 3, 4])
print(case)     #1 (소수 : 7)

print("***********")
case = solution([1, 2, 7, 6, 4])
print(case)     #4 (소수 : 7,11,13,17)