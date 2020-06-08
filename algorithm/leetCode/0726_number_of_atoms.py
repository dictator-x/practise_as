"""
726. Number of Atoms
"""

from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def readAtom(s):
            if not s: return ("", "")
            if not s[0].isupper: return("", s)

            ret = s[0]
            i = 1
            while i < len(s):
                if s[i].islower():
                    ret += s[i]
                else: break
                i += 1

            return (ret, s[i:])

        def readCount(s):
            ret = ""
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    ret += s[i]
                else: break
                i += 1
            return (int(ret), s[i:]) if ret else (1, s)

        def parse(s):
            remaining = s
            ctx = defaultdict(lambda: 0)
            while remaining:
                if remaining[0] == "(":
                    sub_ctx, remaining = parse(remaining[1:])
                    factor, remaining = readCount(remaining)
                    for key in sub_ctx.keys():
                        ctx[key] += sub_ctx[key] * factor
                elif remaining[0] == ")":
                    return (ctx, remaining[1:])
                else:
                    name, remaining = readAtom(remaining);
                    print(remaining)
                    count, remaining = readCount(remaining)
                    ctx[name] += count

            return (ctx, remaining)


        ctx = parse(formula)[0]
        ret = ""
        for key in sorted([ i for i in ctx.keys() ]):
            ret += key
            ret += str(ctx[key]) if ctx[key] > 1 else ""

        return ret
