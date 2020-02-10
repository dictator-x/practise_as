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
        return ord(ch) - ord('a')

    def insert(self, key):

        nextNode = self.root
        length   = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not nextNode.children[level]:
                nextNode.children[level] = self.getNode()
            nextNode = nextNode.children[level]

        nextNode.isEndOfWord = True

    def search(self, key):

        nextNode = self.root
        length = len(key)

        for level in range(length):
            index = self._charToIndex(key[level])
            if not nextNode.chilren[level]:
                return False
            nextNode = nextNode.children[level]

        return nextNode != null and nextNode.isEndOfWord

def main():

if __name__ == '__main__':
    print ("I am main")
