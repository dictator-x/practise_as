"""
269. Alien Dictionary
"""

from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:


        inDegree = {}
        child = {}
        chars = []

        for word in words:
            for char in word:
                child[char] = set([])
                if char not in chars:
                    chars.append(char)

        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]

            if len(first)>len(second) and first[:len(second)] == second:
                return ""

            size = len(first) if len(first) < len(second) else len(second)
            for j in range(size):
                p = first[j]
                c = second[j]
                if p != c:
                    if c not in child[p]:
                        child[p].add(c)
                        if c not in inDegree:
                            inDegree[c] = 1
                        else:
                            inDegree[c] += 1
                    break

        queue = []
        result = []

        print(child)
        print(inDegree)

        for char in chars:
            # I do not think it is make sense
            if char not in inDegree or inDegree[char] == 0:
                queue.append(char)

        print(queue)
        while len(queue) > 0:
            #BFS?
            node = queue.pop()
            result.append(node)
            children = child[node]
            for c in children:
                print(c)
                inDegree[c] -= 1
                if inDegree[c] == 0:
                    queue.append(c)

        return "".join(result) if len(result) == len(chars) else ""



if __name__ == "__main__":
    input = ["za","zb","ca","cb"]
    print("Alien Dictionary")
    solution = Solution()
    print(solution.alienOrder(input))
