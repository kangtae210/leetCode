# 배열 array의 i번째 숫자부터 j번째 숫자까지 
# 자르고 정렬했을 때, k번째에 있는 수
def do(array, command):
    array = array[command[0]-1:command[1]]
    array.sort()
    return array[command[2]-1]

def solution(array, commands):
    ret_val = []
    for i in range(len(commands)):
        target = do(array, commands[i])
        ret_val.append(target)

    return ret_val


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
case = solution(array, commands)
print(case)     #[5, 6, 3]