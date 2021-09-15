# Problem9
# 주어진 정수 x에 대하여 x가 palindrome 정수인지 판단하라.
# palindrome 정수란, 그냥 읽어도, 거꾸로 읽어도 같은 값인 정수이다.
# 다음은 예시이다.
# 121 => True
# -121 => False
# 10 => False
# -101 => False

# 추가적으로, 숫자값을 문자열로 변환하지 않고 해결할 수 있는가?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_x = x
        # 음의 값은 반드시 False
        if x <0:
            return False
        
        #10의 배수는 반드시 False(단, 0은 제외)
        if x % 10 == 0:
            if x != 0:
                return False

        # 거꾸로 읽은 값
        rev_x = 0
        while True:
            rev_x = rev_x * 10 + x % 10
            x = int(x / 10)
            if x == 0:
                break
        
        print(rev_x)

        # 판정 영역
        if is_x == rev_x:
            return True
        else :
            return False





ex = Solution().isPalindrome(12321)
print(ex)