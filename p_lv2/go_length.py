# 5 X 5 좌표평면에 들어가면
def solution(dirs):
    x1, y1 = 0, 0
    x2, y2 = 0, 0
    pass_route = []

    for i in range(len(dirs)):
        x1, y1 = x2, y2

        # 좌표를 옮긴다
        if dirs[i] == 'U':
           y2 = y1 + 1
        elif dirs[i] == 'D':
            y2 = y1 - 1
        elif dirs[i] == 'L':
            x2 = x1 - 1
        else:
            x2 = x1 + 1

        # 만약 정해진 범위(5 X 5)를 넘어서면 이동하지 못하게 조정해준다.
        # 움직이지 않았으므로 경로를 표시하는 배열 pass_route에 추가하지 않고 continue한다.
        if x1 == 5 and x2 == 6:
            x2 = 5
            continue
        if x1 == -5 and x2 == -6:
            x2 = -5
            continue
        if y1 == 5 and y2 == 6:
            y2 = 5
            continue
        if y1 == -5 and y2 == -6:
            y2 = -5
            continue
        
        # 만약 이동 경로가 이미 움직인 경로가 아니면 경로 배열에 추가한다.
        # 좌표 A -> 좌표 B와 좌표 B -> 좌표 A는 동일한 경우이므로 둘 다 추가한다.
        # 따라서 반환시 경로 배열의 크기를 2로 나눈 값을 반환한다.
        if [x1, y1, x2, y2] not in pass_route:
            pass_route.append([x1, y1, x2, y2])
            pass_route.append([x2, y2, x1, y1])
    

    return len(pass_route) // 2






# U  L  U  R  R  D  L  L  U
# L  U  L  L  L  L  L  L  U

dirs = "ULURRDLLU"
case = solution(dirs)
print(case)     # 7

print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

dirs = "LULLLLLLU"
case = solution(dirs)
print(case)     # 7