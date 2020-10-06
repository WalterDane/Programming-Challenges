#https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s: 
            if not stack:
                stack.append(char)
            else:
                if ('(' == stack[-1] and char == ')') or ('[' in stack[-1] and char == ']') or ('{' in stack[-1] and char == '}'):
                    stack.pop()
                else:
                    stack.append(char)
        if not stack:
            return True
        else:
            return False