# 정렬된 두 리스트를 결합하여 
# 새로운 정렬된 리스트를 return하는
# 함수를 작성하라.

class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        answer = []
        # 최초의 노드를 선언한다.
        # if l1[0] < l2[0]:
        #    answer.append(l1[0])
        #    del(l1[0])
        # else:
        #     answer.append(l2[0])
        #     del(l2[0])
        
        # 크기를 비교하여 추가로 삽입한다.
        count = len(l1) + len(l2) -2
        for i in range(count):
            if(len(l1) != 0) and (len(l2) != 0):
                if l1[0] < l2[0]:
                    answer.append(l1[0])
                    del(l1[0])
                else :
                    answer.append(l2[0])
                del(l2[0])

            print("l1=>" , l1)
            print("l2=>" , l2)
            print("ans =",answer)
            print("********************")
            
        print("l1 =>",l1)
        print("l2 =>",l2)
        if len(l1) == 0:
            for i in l2:
                answer.append(i)
        else:
            for i in l1:
                answer.append(i)


        return answer
    


list1 = []
list2 = [0]


sol = Solution()
ex = sol.mergeTwoLists(list1, list2)
print(ex)

