"""
1044. Longest Duplicate Substring
"""

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # Important
        def search(hash_len, a, modulus, nums):
            h = 0
            L = hash_len
            # calculate initial hash.
            for i in range(hash_len):
                h = (h * a + nums[i]) % modulus
            seen = {h}
            al = (a ** L) % modulus

            for i in range(1, n - L + 1):
                # recalculate rolling hash for each slice.
                h = (h*a - nums[i-1]*al + nums[i+L-1]) % modulus
                if h in seen:
                    # find repeat
                    return i
                seen.add(h)

            return -1

        n = len(S)
        nums = [ ord(S[i]) - ord('a') for i in range(n) ]
        a = 26
        # modulus used to control colission
        modulus = 2 ** 32

        # start position is important
        l, h = 1, n
        while l <= h:
            hash_len = l + (h - l) // 2

            if search(hash_len, a, modulus, nums) == -1:
                h = hash_len - 1
            else:
                l = hash_len + 1

        idx = search(l-1, a, modulus, nums)
        return S[idx:idx+l-1]
