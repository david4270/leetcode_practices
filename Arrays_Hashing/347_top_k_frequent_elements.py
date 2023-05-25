# 347. Top K Frequent Elements - Medium - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
        returnlist = []
        for i in nums:
            if i not in numdict:
                numdict[i] = 1
            else:
                numdict[i] = numdict[i] + 1
        
        newnumdict = dict(sorted(numdict.items(), key = lambda item: item[1], reverse = True))
        ctr = 0

        for i in newnumdict.keys():
            if(ctr == k):
                return returnlist
            else:
                returnlist.append(i)
                ctr = ctr + 1
        
        return returnlist