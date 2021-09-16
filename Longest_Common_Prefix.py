# Problem 14
# 문자열들의 배열에서 
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        len_count = len(strs)

        # 길이가 가장 작은 문자열을 기준으로 비교하여
        # index error를 막는다
        strs.sort()     

        len_first_str = len(strs[0])
        answer_str = ""
        
        # 배열의 첫번째 문자열과 비교한다
        for i in range(len_first_str):
            count = 0
            # 첫번째 문자열의 i번째 값을
            # j번째 문자열의 i번째 값과 비교한다.
            for j in range(len_count -1):
                if strs[j+1][i] == strs[0][i]:
                    count += 1
                else:
                    return answer_str
            
            answer_str += strs[0][i]
        
        return answer_str

                






str = ["abab", "aba", ""]

sol = Solution()
ex = sol.longestCommonPrefix(str)

print(ex)



        # for i in range(len_first_str):
        #     count = 0
        #     for j in range(len_count-1):
        #         if strs[0][i] == strs[j+1][i]:
        #             count += 1
        #         else:
        #             break
        #     if count == len_count-1:
        #         answer_str += strs[0][i]
        #     else:
        #         return answer_str
        # if len_count == 1:
        #     return strs[0]
        # if len_first_str == 0:
        #     return ''
        # return answer_str