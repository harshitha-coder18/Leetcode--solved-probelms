class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            else:
                if not stack:
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':
                    return False
                if ch == ']' and top != '[':
                    return False
                if ch == '}' and top != '{':
                    return False

        if not stack:
            return True
        else:
            return False