class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returnList = []
        nums.sort()

        pta, ptb = 0, 0
        sumNum = 0
        #for i in range(0,1):
        for i in range(0,len(nums)-1):
            
            if nums[i] == nums[i-1] and i>0:
                continue
            pta = i + 1
            ptb = len(nums) - 1
            while pta < ptb:
                
                if nums[i] + nums[pta] + nums[ptb] == 0:
                    
                    
                    """
                    if templist not in returnList:
                        returnList.append(templist)
                    """
                    
                    if nums[pta] == nums[pta+1] and pta+1 != ptb:
                        #print(i,pta,ptb,"skipped")
                        pta = pta + 1
                        continue
                    elif nums[ptb] == nums[ptb-1] and ptb-1 != pta:
                        #print(i,pta,ptb,"skipped")
                        ptb = ptb - 1
                        continue
                    else:
                        #print(i,pta,ptb)
                        templist = [nums[i], nums[pta], nums[ptb]]
                        returnList.append(templist)
                        pta = pta + 1
                    #continue
                elif nums[i] + nums[pta] + nums[ptb] > 0:
                    ptb = ptb - 1
                else:
                    pta = pta + 1
            
                
        return returnList