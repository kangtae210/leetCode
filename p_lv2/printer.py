def solution(priorities, location):
    length = len(priorities)
    idx = [i for i in range(length)]

    answer = []
    while True:
        if len(priorities) == 0:
            break
            
        if priorities[0] != max(priorities):
            priorities = priorities[1:] + [priorities[0]]
            idx = idx[1:] + [idx[0]]
        else:
            priorities = priorities[1:]
            answer.append(idx[0])
            idx = idx[1:]

        try:
            if answer[-1] == location:
                break
        except:
            continue



    return len(answer)





print(solution(priorities=[2, 1, 3, 2], location=2))        # 1
print("======================")
print(solution(priorities=[1, 1, 9, 1, 1, 1], location=0))  # 5
