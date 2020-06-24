"""
609. Find Duplicate File in System
"""

from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_file = defaultdict(list)

        for path in paths:
            s_path = path.split("/")
            f = s_path.pop()
            files = f.split(" ")
            s_path.append(files.pop(0))

            for file in files:
                file_name = file[:file.find("(")]
                file_content = file[file.find("(")+1:file.find(")")]
                content_file[file_content].append("/".join(s_path)+"/"+file_name)

        ret = []
        for key, val in content_file.items():
            if len(val) >= 2:
                ret.append(val)

        return ret
