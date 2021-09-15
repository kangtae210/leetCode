#정수 가 주어졌을 때 자리가 변경된 x를 반환하라.

class Solution(object):
    def reverse(self, x):
        digit_list = []
        answer = 0
        minus = 0
        if x < 0:
            x = -x
            minus = 1
        

        
        while True:
            digit_list.append(x % 10)
            x = int(x / 10)
            if x / 10 == 0:
                break
        print(digit_list)
        for i in range(len(digit_list)):
            answer += digit_list[i] * (10 ** (len(digit_list) - (i+1)))
        
        answer = answer * ((-1) ** minus)

        if answer > (2 ** 31) - 1:
            return 0
        elif answer < -(2**31):
            return 0
        else:
            return answer





sol = Solution()
answer = sol.reverse(1463847412)
print(answer)


value = 1463847412

value_b = format(value, '#b')
print(value_b)
print(len(value_b))





