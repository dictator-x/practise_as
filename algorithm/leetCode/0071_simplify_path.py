"""
71. Simplify Path
"""

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        splits = path.split("/")

        for s in splits:
            if s == "" or s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)


        return "/" + "/".join(stack)
