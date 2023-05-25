# 20. Valid Parentheses - Easy - https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {']':'[', '}':'{',')':'('}
        stack = []
        for c in s:
            if c not in mapping:
                stack.append(c)
                continue #next iteration
            if not stack:
                return False
            if stack[-1] != mapping[c]:
                return False
            stack.pop()
        return not stack