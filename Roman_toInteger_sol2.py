class Solution:
    def romanToInt(self, s : str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        answer = 0
        for i in range(len(s)-1):
            temp = 1
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                temp = -1
            answer += roman_dict[s[i]] * temp
        answer += roman_dict[s[-1]]
        return answer

sol = Solution()
ex = sol.romanToInt('MCMXCIV')
print(ex)