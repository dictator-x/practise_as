"""
1153. String Transforms Into Another String
"""
class Solution:
    # Import case: when str1 or str2 has 26 letter
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True

        dp = {}
        record = set()
        for i in range(len(str1)):
            if str1[i] not in dp:
                dp[str1[i]] = str2[i]
            else:
                if dp[str1[i]] != str2[i]:
                    return False
            record.add(str2[i])
        if len(dp.keys()) < 26 or len(record) < 26: return True
        return False
