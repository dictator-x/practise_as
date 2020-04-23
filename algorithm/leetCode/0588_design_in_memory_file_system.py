"""
588. Design In-Memory File System
"""

from typing import List

class File:
    def __init__(self, isFile=False):
        self.isFile = isFile
        self.files = {}
        self.content = ""

class FileSystem:

    def __init__(self):
        self.root = File()

    def convertPath(self, path):
        ret = path.split("/")
        while not len(ret) <= 0 and ret[0] == "":
            ret.pop(0)
        return ret

    def ls(self, path: str) -> List[str]:
        head = self.root
        paths = self.convertPath(path)

        for p in paths:
            head = head.files[p]

        if head.isFile:
            return [paths[-1]]
        else:
            ret = []
            for key in head.files:
                ret.append(key)
            return sorted(ret, key=lambda name: name)

    def mkdir(self, path: str) -> None:
        head = self.root
        paths = self.convertPath(path)

        for p in paths:
            if p not in head.files:
                head.files[p] = File()
            head = head.files[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        head = self.root
        paths = self.convertPath(filePath)

        for p in paths[:-1]:
            head = head.files[p]

        if paths[-1] not in head.files:
            newFile = File(True)
            newFile.content = content
            head.files[paths[-1]] = newFile
        else:
            head.files[paths[-1]].content += content

    def readContentFromFile(self, filePath: str) -> str:
        head = self.root
        paths = self.convertPath(filePath)

        for p in paths[:-1]:
            head = head.files[p]

        return head.files[paths[-1]].content








