"""
770. Basic Calculator IV
"""

from typing import List
import re

# expr->term {'+'|'-'} expr | term : lowest priority
# term->item '*' term | item
# item->var | num | '(' expr ')': highest prority

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        dic = dict(zip(evalvars, evalints))
        # Record power of a var
        times = {"": 0}

        num = r"(?P<NUM>[0-9]+)"
        var = r"(?P<VAR>[a-z]+)"
        plus = r"(?P<PLUS>\+)"
        sub = r"(?P<SUB>\-)"
        multi = r"(?P<MULTI>\*)"
        left = r"(?P<LEFT>\()"
        right = r"(?P<RIGHT>\))"
        pattern = re.compile("|".join([num,var,plus,sub,multi,left,right]))

        def genToken(s):
            for a in pattern.finditer(s):
                yield next(filter(lambda x:x[1],a.groupdict().items()))

        tokens = list(genToken(expression))
        n = len(tokens)
        self.i = 0

        # Doing add
        # a and b are dict
        # this will calculate occurrance of each key
        # key: "" represents number
        def add(a, b, isadd):
            ak = set(a.keys())
            for k in ak:
                if isadd:
                    a[k] += b.get(k, 0)
                else:
                    a[k] -= b.get(k, 0)
                # if occurrance is zero means that expr*0
                if a[k] == 0:
                    a.pop(k)
            # handle case for key in b not in a
            for k in b:
                if k not in ak:
                    if isadd:
                        a[k] = b[k]
                    else:
                        a[k] = -b[k]
            return a

        # product of two dicts
        def multi(a, b):
            res = {}
            import itertools
            for k1, k2 in itertools.product(a, b):
                # handle key in k1 not in k2
                if k1 == "":
                    nk = k2
                elif k2 == "":
                    nk = k1
                else:
                    nk = "*".join(sorted(k1.split("*") + k2.split("*")))
                res[nk] = res.get(nk, 0) + a[k1] * b[k2]
                times[nk] = times[k1] = times[k2]
            return res

        # item->var | num | '(' expr ')'
        def item():
            t, token = tokens[self.i]
            # item -> num
            if t == "NUM":
                self.i += 1
                return {"":int(token)}
            # item -> var
            if t == "VAR":
                self.i += 1
                if token in dic:
                    return {"":dic[token]}
                times[token] = 1
                return {token: 1}
            # item -> '(' expr ')'
            self.i += 1
            res = expr({}, True)
            self.i += 1
            return res

        # term->item '*' term | item
        def term():
            # term -> item
            now = item()
            # term -> item '*' term
            while self.i < n:
                t, token = tokens[self.i]
                if t == "MULTI":
                    self.i += 1
                    now = multi(now, term())
                else:
                    break
            return now

        # expr->term {'+'|'-'} expr | term
        def expr(now, isadd):
            # expr -> term
            now = add(now, term(), isadd)
            # expr->term {'+'|'-'} expr
            if self.i < n:
                t, token = tokens[self.i]
                if t == "PLUS" or t == "SUB":
                    self.i += 1
                    return expr(now, token == "+")
            return now

        res = expr({}, True)
        # print(res)
        # return []

        ret = list(map(lambda x: "%d%s" % (res[x], ("*%s"%x) if len(x) else ""), sorted(filter(lambda x:res[x]!=0 and x != "",res.keys()),key=lambda x:(-len(x.split("*")), tuple(x.split("*")),-times[x]))))

        if "" in res and res[""] != 0:
            return ret + [str(res[""])]
        else:
            return ret

if __name__ == "__main__":
    exp = "e + 8 - a + 5"
    evalvars = ["e"]
    evalints = [1]
    solution = Solution()
    print(solution.basicCalculatorIV(exp, evalvars, evalints))

