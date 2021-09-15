# Problem 1
# 정수 리스트 nums와 정수 target이 주어져있다.
# 리스트 nums의 두 원소를 합하면 target 값이 되는
# 두 지수값을 리스트로 하는 리스트 rtype을 반환하는 함수를 작성하라.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rtype = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    rtype.append(i)
                    rtype.append(j)
        return rtype[0:2]