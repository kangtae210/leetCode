# Problem 20
# 유효한 괄호인지 판별하는 함수 isValid를 작성하라
# 조건 1) 괄호가 열렸다면 같은 괄호종류로 닫혀야한다.
# 조건 2) 열린 괄호는 옳은 위치에서 닫혀야한다.
# ( 와 )의 조합
# { 와 }의 조합
# [ 와 ]의 조합

class Solution:
    stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):      # 가장 마지막에 삽입한 데이터를 삭제
        if self.isEmpty() == False:
            print("Stack is Empty")
        else:
            del self.stack[-1]

    def top(self):      # 가장 마지막에 삽입한 데이터를 삭제하지 않고 return
        if self.isEmpty() == False:
            return "Stack is Empty"
        else:
            return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return False        # 스택이 비어있다면 False
        else:
            return True         # 스택에 값이 있으면 Ture



    def isValid(self,s :str) -> bool:
        #괄호가 열렸다가 닫히면 문자열의 크기는 짝수이다.
        if (len(s) %2 == 1):
            return False

        # 괄호문자의 짝을  mapping하는 자료
        char_dict = [
            ['(', ')'],
            ['{', '}'],
            ['[', ']']
            ]


        for i in range(len(s)):                             # string의 각 원소별로 접근
            for j in range(3):
                if s[i] == char_dict[j][0]:                 # 원소가 왼쪽 괄호에 해당한다면 스택에 push
                    self.push(s[i])       
                if s[i] == char_dict[j][1]:               # 오른쪽 괄호 x에 해당한다면 
                    check = self.top()                      # 스택의 마지막 원소를 가져와서
                    
                    if check == char_dict[j][0]:            # 이 값이 x의 짝과 맞는지 확인하고
                        self.pop()                          # 맞다면 pop 메서드로 삭제한다
                    else:                                   # 맞지 않다면 유효하지 않은 괄호 표기이다.
                        return False
        

        if len(self.stack) == 0:
            return True
        else:
            return False
            


        
        

sol = Solution()
ex = sol.isValid("{[]}")
print(ex)