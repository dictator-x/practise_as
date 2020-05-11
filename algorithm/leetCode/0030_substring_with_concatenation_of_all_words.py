"""
30. Substring with Concatenation of All Words
"""
from typing import List
import copy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == "" or not words: return []
        n_words = len(words)
        n_word = len(words[0])
        m_words = {}
        for w in words:
            if w not in m_words:
                m_words[w] = 1
            else:
                m_words[w] += 1

        ret = []
        for i in range(0, len(s) - n_word*n_words+1):
            sub = s[i:i+n_word*n_words]
            count = 0
            find_words = copy.deepcopy(m_words)
            for j in range(0, n_words):
                w = sub[j*n_word: (j+1)*n_word]
                if w not in find_words:
                    break
                if find_words[w] <= 0:
                    break

                count += 1
                find_words[w] -= 1
            if count == n_words:
                ret.append(i)
        return ret

