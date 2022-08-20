class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        list_str = list(s)
        for char in list_str:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                elif stack.pop() == '(':
                    pass
                else:
                    return False
            elif char == '}':
                if not stack:
                    return False
                if stack.pop() == '{':
                    pass
                else:
                    return False
            elif char == ']':
                if not stack:
                    return False
                if stack.pop() == '[':
                    pass
                else:
                    return False
        if not stack:
            return True
            