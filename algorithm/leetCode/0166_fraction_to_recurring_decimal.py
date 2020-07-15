"""
166. Fraction to Recurring Decimal
"""

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return "0"

        ret = ["-"] if numerator*denominator else []

        numerator = abs(numerator)
        denominator = abs(denominator)

        div, mod = divmod(numerator, denominator)
        ret.append(str(div))
        if mod == 0:
            return "".join(ret)

        record = {}
        ret.append(".")
        while mod != 0:
            # TODO: circuit break.
            if mod in record:
                ret.insert(record[mod], "(")
                ret.append(")")
                return "".ret

            record.put(mod, len(ret))
            div, mod = divmod(mod*10, denominator)
            record.put(div)


