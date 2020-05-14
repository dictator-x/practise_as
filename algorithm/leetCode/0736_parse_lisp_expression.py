"""
736. Parse Lisp Expression
"""

class Solution:
    def evaluate(self, expression: str) -> int:

        def tokenize(s):
            t = s.split(" ")
            ret = []
            for item in t:
                l, r = 0, 0
                for c in item:
                    if c == "(":
                        l += 1
                    if c == ")":
                        r += 1
                token = item[l: len(item)-r]
                while l > 0:
                    ret.append("(")
                    l -= 1
                ret.append(token)
                while r > 0:
                    ret.append(")")
                    r -= 1
            return ret

        tokens = tokenize(expression)
        contexts = []

        def findValue(contexts, symbol):
            for i in range(len(contexts)-1, -1, -1):
                if symbol in contexts[i]:
                    return contexts[i][symbol]

        def eval(tokens):
            contexts.append({})
            value = 0
            popBracket = False
            if tokens[0] == "(":
                tokens.pop(0)
                popBracket = True

            token = tokens.pop(0)
            if token == "add":
                value = eval(tokens) + eval(tokens)
            elif token == "mult":
                value = eval(tokens) * eval(tokens)
            elif token == "let":
                while tokens[0] != ")":
                    # last expr
                    if tokens[0] == "(":
                        value = eval(tokens)
                        break

                    var_name = tokens.pop(0)
                    if tokens[0] == ")":
                        if var_name.isdigit() or var_name[0] == "-":
                            print(var_name)
                            value = int(var_name)
                        else:
                            print(var_name)
                            print(contexts)
                            value = findValue(contexts, var_name)
                        break

                    value = eval(tokens)
                    contexts[-1][var_name] = value


            elif token.isdigit() or token[0] == "-":
                value = int(token)
            else:
                # lookup value
                value = findValue(contexts, token)

            if popBracket and tokens[0] == ")": tokens.pop(0)
            contexts.pop()
            return value

        return eval(tokens)
