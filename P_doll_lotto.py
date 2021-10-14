def solution(board, moves):
    answer = 0
    my_dolls = []       # 뽑은 인형들을 저장, 같은 인형이 양옆에 있으면 -1로 표시

    for i in moves:     # 각 명령 실행
        for row in range(len(board)):
            if (board[row][i-1] != 0):
                my_dolls.append(board[row][i-1])
                board[row][i-1] = 0
                if len(my_dolls) >= 2:
                    if my_dolls[-1] == my_dolls[-2]:
                        del my_dolls[-1]
                        del my_dolls[-1]
                        answer += 2
                break

    return answer





board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

for i in board:
    print(i)


case = solution(board, moves)
print(case)     # 4