"""
689. Maximum Sum of 3 Non-Overlapping Subarrays
"""

from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # index range: 0 ... k-1 .... n-k .... < n
        N = len(nums)
        pre_sum = [0]*(N+1)
        for i in range(1, N+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]

        # Initial first value: sum from 0 ... k-1
        total = pre_sum[k] - pre_sum[0]
        # left[0, k-1] is 0, in which 0...k-2 is unmeaningful.
        # left[k-1] is biggest sum from 0 to k-1
        left = [0] * N
        # Record previous k big sub array sum and store index in k+1 position
        for i in range(k, N):
            if pre_sum[i+1] - pre_sum[i-k+1] > total:
                left[i] = i-k+1
                total = pre_sum[i+1] - pre_sum[i-k+1]
            else:
                left[i] = left[i-1]

        right = [N-k] * N
        total = pre_sum[N] - pre_sum[N-k]
        for i in range(N-k-1,-1,-1):
            if pre_sum[i+k] - pre_sum[i] >= total:
                total = pre_sum[i+k] - pre_sum[i]
                right[i] = i
            else:
                right[i] = right[i+1]

        ret = [0, 0, 0]
        total = 0
        for i in range(k, N - 2*k + 1):
            l_idx, r_idx = left[i-1], right[i+k]
            l_sum = pre_sum[l_idx+k] - pre_sum[l_idx]
            r_sum = pre_sum[r_idx+k] - pre_sum[r_idx]
            m_sum = pre_sum[i+k] - pre_sum[i]

            if (l_sum + m_sum + r_sum) > total:
                total = l_sum + m_sum + r_sum
                ret = [l_idx, i, r_idx]

        return ret
