# Python program for insert and search
# operation in a Trie

class TrieNode:

    def __init__(self):
        self.children    = [None]*26
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self, char):
        return ord(char) - ord('a')

    def insert(self, key):

        nextNode = self.root
        length   = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not nextNode.children[index]:
                nextNode.children[index] = self.getNode()
            nextNode = nextNode.children[index]

        nextNode.isEndOfWord = True

    def search(self, key):

        nextNode = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not nextNode.children[index]:
                return False
            nextNode = nextNode.children[index]

        return nextNode != None and nextNode.isEndOfWord

def main():
    keys = ["the","a","there","anaswe","any", "by","their"]
    output = ["Not present in trie", "Present in trie"]

    t = Trie()

    for key in keys:
        t.insert(key)

    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))

if __name__ == '__main__':
    main()
