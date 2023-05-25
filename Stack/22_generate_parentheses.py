# 22. Generate Parentheses - Medium - https://leetcode.com/problems/generate-parentheses/

class Solution:
    def helpGenerate(self, init: str, leftn: int, rightn: int) -> List[str]:
        arr = []
        if leftn == rightn == 0:
            arr = [init]
            print(init)
            return arr
        if leftn > 0:
            arr.extend(self.helpGenerate(init+"(",leftn-1,rightn))
        if rightn > leftn:
            arr.extend(self.helpGenerate(init+")",leftn,rightn-1))
        return arr

    def generateParenthesis(self, n: int) -> List[str]:
        init = "("
        leftn = n-1
        rightn = n

        return self.helpGenerate(init,leftn,rightn)
        