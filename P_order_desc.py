def solution(n):
    n_arr= []
    answer = ""
    for i in str(n):
        n_arr.append(i)
    n_arr.sort(reverse= True)
    for i in n_arr:
        answer += i
    return int(answer)


def solution2(n):
    arr= list(str(n))
    arr.sort(reverse= True)
    
    return int("".join(arr))

case = solution2(118372)
print(case)     #873211



