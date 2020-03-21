"""
126. Word Ladder II
"""

from typing import List
from string import ascii_lowercase

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []

        # Build graph
        # Key point at here is to buld a DAG. So you need a indepth to check
        # each word
        wl = set(wordList)
        queue = [ beginWord ]
        child = {beginWord: set([])}
        find = False
        levels = { beginWord: 1 }
        step = 0

        for w in wl:
            if w not in child:
                child[w] = set([])

        if beginWord in wl:
            wl.remove(beginWord)

        while len(queue) > 0 and not find:
            step += 1
            for i in range(len(queue)):
                word = queue.pop(0)
                for j in range(len(word)):
                    for c in ascii_lowercase:
                        new_word = word[:j] + c + word[j+1:]
                        if new_word == endWord:
                            child[word].add(new_word)
                            find = True
                        elif new_word in levels and step < levels[new_word]:
                            child[word].add(new_word)

                        if new_word not in wl:
                            continue

                        levels[new_word] = step + 1
                        wl.remove(new_word)
                        queue.append(new_word)
                        child[word].add(new_word)

        print (child)

        # DFS find path
        if not find:
            return []

        ret = []
        def findPath(prefix, word):
            if word == endWord:
                ret.append(prefix[:])
                return
            if word not in child:
                return
            for w in child[word]:
                prefix.append(w)
                findPath(prefix, w)
                prefix.pop()
        findPath([beginWord], beginWord)

        return ret


if __name__ == "__main__":
    # beginWord = "a"
    # endWord = "c"
    # wordList = ["a","b","c"]
    beginWord = "hot"
    endWord = "dog"
    wordList = ["hot","dog","dot"]
    solution = Solution()
    print(solution.findLadders(beginWord, endWord, wordList))
