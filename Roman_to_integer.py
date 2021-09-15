# 로마 숫자를 아라비아 숫자값으로 바꾸는 함수를 작성하라.
# I => 1
# V => 5
# x => 10
# L => 50
# C => 100
# D => 500
# M => 1000
# I는 V와 X 앞에 붙어 4, 9를 표현한다.
# X는 L과 C 앞에 붙어 40, 90을 표현한다.
# C는 D와 M 앞에 붙어 400, 900을 표현한다.
class Solution:
    def romanToInt(self, s : str) -> int:
        answer = 0
        roman_careful_dict = {
            'IV' : 4,
            'IX' : 9, 
            'XL' : 40,             
            'XC' : 90, 
            'CD' : 400, 
            'CM' : 900
        }
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        
        # 주의해야할 로마값이 있는지 확인
        # 있으면 제거
        for i in range(len(s)):
            print(i)
            check_str = s[i:i+2]
            print(check_str)
            if check_str in roman_careful_dict:
                answer += roman_careful_dict[check_str]
                s = s.replace(check_str,"aa", 1)
                i = i-2       

        
        for i in s:
            if i in roman_dict:
                answer += roman_dict[i]
                s = s.replace(i, "", 1)

        return answer


ex = Solution()
result = ex.romanToInt('LVIII')
print(result)
