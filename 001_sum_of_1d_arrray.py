class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [] # create a new empty list
        r = 0
        for v in nums:
            r += v
            result.append(r)
        return result
        
# 可读性0
# 时间复杂度
# 空间复杂度
