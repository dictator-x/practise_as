"""
282. Expression Add Operators
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num: return []
        n = len(num)
        ret = []
        ops = [ "*", "+", "-", "" ]

        def calculateExp(exp):
            exp = exp + "+0"
            op_pre = "+"
            val = 0
            stack = []

            for c in exp:
                if c.isdigit():
                    val = val * 10 + int(c)
                else:
                    if op_pre == "+":
                        stack.append(val)
                    elif op_pre == "-":
                        stack.append(-1*val)
                    else:
                        ret_mul = val * stack.pop()
                        stack.append(ret_mul)

                    val = 0
                    op_pre = c

            return sum(stack)


        def search(exp, idx, value_start_idx):
            if idx == n:
                # print(exp)
                ret_exp = calculateExp(exp)
                if ret_exp == target: ret.append(exp)
                return

            for op in ops:
                if op != "":
                    search(exp + op + num[idx], idx + 1, idx)
                elif op == "" and num[value_start_idx] != "0":
                    search(exp + op + num[idx], idx + 1, value_start_idx)

        search(num[0], 1, 0)

        return ret
