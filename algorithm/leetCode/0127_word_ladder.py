"""
127. Word Ladder
"""

from typing import List
from string import ascii_lowercase

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wl = set(wordList)
        queue = [beginWord]
        level = 0

        while len(queue) > 0:
            for i in range(len(queue)):
                word = queue.pop(0)
                if ( word == endWord ):
                    return level + 1

                for j in range(len(word)):
                    for c in ascii_lowercase:
                        new_word = word[:j] + c + word[j+1:]
                        if new_word in wl:
                            queue.append(new_word)
                            wl.remove(new_word)
            level += 1

        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    solution = Solution()
    print(solution.ladderLength(beginWord, endWord, wordList))
