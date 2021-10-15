# 현재 손의 상태 : 왼손(*), 오른손(#)
# 1, 4, 7    => 왼손
# 3, 6, 9    => 오른손
# 2, 5, 8, 0 => 가까운 손가락
# 거리가 같다면 왼손잡이는 왼손, 오른손잡이는 오른손 사용
def move(number, left, right, hand) :
    left_d = 0
    right_d = 0
    if number == 2 :
        left_d = abs(left[0] - 0) + abs(left[1] - 1)
        right_d = abs(right[0] - 0) + abs(right[1] - 1)
    if number == 5 :
        left_d = abs(left[0] - 1) + abs(left[1] - 1)
        right_d = abs(right[0] - 1) + abs(right[1] - 1)   
    if number == 8 :
        left_d = abs(left[0] - 2) + abs(left[1] - 1)
        right_d = abs(right[0] - 2) + abs(right[1] - 1) 
    if number == 0 :
        left_d = abs(left[0] - 3) + abs(left[1] - 1)
        right_d = abs(right[0] - 3) + abs(right[1] - 1)


    if left_d > right_d:
        return "R"
    elif left_d < right_d:
        return "L"
    else:
        return hand[0].upper()


def solution(numbers, hand):
    answer = ''
    left = [3, 0]
    right = [3, 2]


    for i in range(len(numbers)):

        if numbers[i] in [1, 4, 7]:
            answer += 'L'
            left[0] = numbers[i] // 3
            left[1] = 0
        elif numbers[i] in [3, 6, 9]:
            answer += 'R'
            right[0] = numbers[i] // 3 -1
            right[1] = 2

        else:
            target = move(numbers[i], left, right, hand)
            answer += target
            if numbers[i] == 0 :
                if target == "L":
                    left[0] = 3
                    left[1] = 1
                else:
                    right[0] =3
                    right[1] = 1
            else:
                if target == "L":
                    left[0] = numbers[i] // 3
                    left[1] = 1
                else:
                    right[0] = numbers[i] // 3
                    right[1] = 1
  
    return answer






case = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(case)   # "L  R  L  L  L  R  L  L  R  R  L"
              #  L  R  L  L  L  R  L  L  L  R  L  

case = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 	"left")
print(case)   # "L  R  L  L  R  R  L  L  L  R  R"
              #  L  R  L  L  R  R  L  L  L  R  R

case = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 	"right")
print(case)   # "L  L  R  L  L  R  L  L  R  L"
              #  L  L  R  L  L  R  L  L  R  R  






