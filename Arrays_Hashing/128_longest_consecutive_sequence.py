# 128. Longest Consecutive Sequence - Medium - https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        ctr = 1
        maxctr = 1
        lenNums = len(nums)
        if lenNums < 2:
            return lenNums
        for i in range(0,lenNums-1):
            if nums[i+1] != nums[i] + 1:
                if ctr > maxctr:
                    maxctr = ctr
                ctr = 1
            else:
                ctr += 1
        
        if ctr > maxctr:
            maxctr = ctr
        return maxctr