"""
811. Subdomain Visit Count
"""

from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counters = defaultdict(lambda: 0)
        for cp in cpdomains:
            count, domain = cp.split(" ")
            count = int(count)
            frags = domain.split(".")
            for i in range(len(frags)):
                counters[".".join(frags[i:])] += count
        return [ "{} {}".format(ct, dom) for dom, ct in counters.items()]
