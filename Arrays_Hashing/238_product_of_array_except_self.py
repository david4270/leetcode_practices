# 238. Product of Array Except Self - Medium - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftmul = [1] * len(nums)
        rightmul = [1] * len(nums)
        solution = [1] * len(nums)
        for i in range(1, len(nums)):
            leftmul[i] = leftmul[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            rightmul[i] = rightmul[i+1] * nums[i+1]
        for i in range(0, len(nums)):
            solution[i] = leftmul[i] * rightmul[i]
        return solution
            