class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(":")", "[":"]", "{":"}"}
        stack = []

        for i in s:
            if i in matches:
                stack.append(i)
            else:
                if not stack:
                    return False
                open_br = stack.pop()
                if matches[open_br] != i:
                    return False

        return not stack