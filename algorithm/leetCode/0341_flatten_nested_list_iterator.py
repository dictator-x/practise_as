"""
341. Flatten Nested List Iterator
"""

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        list = []
        def retrieve(nestedList):
            for l in nestedList:
                if l.isInteger():
                    list.append(l.getInteger())
                else:
                    retrieve(l.getList())
        retrieve(nestedList)
        print(list)
        self.list = list
        self.position = -1

    def next(self) -> int:
        self.position += 1
        return self.list[self.position]

    def hasNext(self) -> bool:
        return True if self.position + 1 < len(self.list) else False
