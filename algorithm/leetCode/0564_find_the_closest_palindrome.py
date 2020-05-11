"""
564. Find the Closest Palindrome
"""
import sys

class Solution:
    def nearestPalindromic(self, s: str) -> str:
        n = len(s)
        def mirror(s):
            n = len(s)
            l_part = s[0:n//2]
            md = s[n//2] if n % 2 == 1 else ""
            return l_part + md + l_part[::-1]

        if s == "1": return "0"

        p1 = mirror(s)
        diff1 = abs(int(p1) - int(s))
        # We should ignore equal case
        diff1 = sys.maxsize if diff1 == 0 else diff1

        # consider cases if s is panlindrome already.
        md = (n - 1) // 2
        i = md
        l_s = [c for c in s]
        # change
        while i >= 0 and l_s[i] == "0":
            l_s[i] = "9"
            i -=1

        if i == 0 and l_s[i] == '1':
            l_s.pop(0)
            l_s[(len(s)-1)//2]= "9"
        else:
            l_s[i] = str(int(l_s[i])-1)

        p2 = mirror("".join(l_s))
        diff2 = abs(int(s)-int(p2))

        md = (n - 1) // 2
        i = md
        l_s = [c for c in s]
        # change
        while i >= 0 and l_s[i] == "9":
            l_s[i] = "0"
            i -= 1

        if i < 0:
            l_s.insert(0,"1")
        else:
            l_s[i] = str(int(l_s[i])+1)

        p3 = mirror("".join(l_s))
        diff3 = abs(int(s)-int(p3))
        print(p1,p2,p3)
        print(diff1,diff2,diff3)

        if diff2 <= diff1 and diff2 <= diff3:
            return p2
        if diff1 <= diff3 and diff1 <= diff2:
            return p1
        else:
            return p3

