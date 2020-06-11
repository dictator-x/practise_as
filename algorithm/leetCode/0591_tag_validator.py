"""
591. Tag Validator
"""
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        while i < len(code):
            if i > 0 and not stack: return False
            if code.startswith("<![CDATA[", i):
                j = i + 9
                i = code.find("]]>", j)
                if i == -1: return False;
                i += 3
            elif code.startswith("</", i):
                j = i + 2
                i = code.find(">", j)
                if i == -1 or i - j > 9 or i == j: return False
                if not code[j:i].isupper() or not code[j:i].isalpha():
                    return False
                substr = code[j:i]
                if not stack or not substr == stack.pop():
                    return False
                i += 1
            elif code.startswith("<", i):
                j = i + 1
                i = code.find(">", j)
                if i == -1 or i - j > 9 or i == j: return False
                if not code[j:i].isupper() or not code[j:i].isalpha():
                    return False
                stack.append(code[j:i])
                i += 1
            else:
                i += 1

        return not stack

