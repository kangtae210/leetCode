# 스택 구현

# 스택 구현

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):      # 가장 마지막에 삽입한 데이터를 삭제
        if self.stack.isEmpty() == False:
            print("Stack is Empty")
        else:
            self.stack.remove(self.stack[-1])
            print("삭제완료")

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


st = Stack()


print(st.stack)

x = st.top()
print(x)






