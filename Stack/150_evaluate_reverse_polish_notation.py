# 150. Evaluate Reverse Polish Notation - Medium - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens:
            tk  = tokens.pop(-1)
            
            if tk not in {'+','-','*','/'}:
                return int(tk)
            
            b = self.evalRPN(tokens)
            a = self.evalRPN(tokens)
                
            if tk == '+':
                return(a + b)
            elif tk == '-':
                return (a - b)
            elif tk == '*':
                return (a * b)
            else:
                return (int(a / b))
            
        return 0