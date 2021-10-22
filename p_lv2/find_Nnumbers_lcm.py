def gcd(a,b):
    if a<b:
        a, b = b, a
    
    r = a % b

    if r==0:
        return b
    else:
        return gcd(b,r)

def solution(arr):
    lcm = 1
    for i in range(len(arr)):
        lcm = lcm * arr[i] /gcd(lcm, arr[i])

    return int(lcm)



case = solution([2,6,8,14])
print(case)     # 168


print("*****************")
case = solution([3, 4, 9, 16])
print(case)     # 144