def change(nth, number):
    num_strs = ['0', '1', '2','3', '4', '5','6', '7', '8','9', 'A', 'B','C', 'D', 'E','F']
    answer = ""
    while True:
        answer = num_strs[number % nth] + answer
        number = number // nth

        if (number == 0):
            break
        pass
    return answer

# 진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 
def solution(n, t, m, p):
    string = ""

    for i in range(t*(m+1)):
        string += change(n, i)

        
    answer = ""
    for i in range(t):
        answer += string[i * m + p-1]
   
    return answer
 #튜브가 말해야 하는 숫자 t개를 공백 없이 차례대로 나타낸 문자열. 
 # 단, 10~15는 각각 대문자 A~F로 출력한다.







case = solution(2, 4, 2, 1)
print(case)         #"0111"

case = solution(16, 16, 2, 1)
print(case)         #"02468ACE11111111"

case = solution(16, 16, 2, 2)
print(case)         #"13579BDF01234567"



