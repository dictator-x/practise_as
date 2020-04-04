"""
212. Word Search II
"""

from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        class TrieNode:
            def __init__(self):
                self.chars = [None] * 26
                self.completeWord = None

        wl = set(words)
        r, c = len(board), len(board[0])

        # Build trie.
        root = TrieNode()
        for word in wl:
            temp = root
            for char in word:
                offset = ord(char) - ord("a")
                # Only create new node if not exists
                if temp.chars[offset] == None:
                    temp.chars[offset] = TrieNode()
                temp = temp.chars[offset]
            temp.completeWord = word

        ret = set([])
        def doFind(i, j, root):
            if i < 0 or j < 0 or i == r or j == c or board[i][j] == "#":
                return

            char = board[i][j]
            cur = root.chars[ord(char) - ord("a")]
            if cur == None:
                return

            if cur.completeWord != None:
                ret.add(cur.completeWord)

            board[i][j] = "#"
            doFind(i-1, j, cur)
            doFind(i+1, j, cur)
            doFind(i, j-1, cur)
            doFind(i, j+1, cur)
            board[i][j] = char


        for i in range(r):
            for j in range(c):
                doFind(i, j, root)

        return ret


if __name__ == "__main__":
    # board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    # words = ["oath","pea","eat","rain"]
    # board = [['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']]
    # words = ["oath","pea","eat","rain"]
    board = [["a","b"],["c","d"]]
    words = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
    solution = Solution()
    print(solution.findWords(board, words))
