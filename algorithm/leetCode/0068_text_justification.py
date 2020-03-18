"""
68. Text Justification
"""

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        ret = []

        while len(words) > 0:
            start_word = words[0]
            start = 0
            end = start + 1
            cur_len = len(start_word)

            while ( end < len(words) ) and ( cur_len + len(words[end]) + 1 ) <= maxWidth:
                # print(cur_len)
                cur_len += 1 + len(words[end])
                end += 1

            num_words = end - start
            extra_space = maxWidth - cur_len
            intervals = num_words - 1
            line = ""
            start_word = words.pop(0)

            if intervals == 0:
                line = start_word + " "*(maxWidth - len(start_word))
            elif intervals >= len(words):
                line = start_word
                while len(words) != 0:
                    line += " " + words.pop(0)
                line += " "*(maxWidth -len(line))
            else:
                line = start_word
                extra_space_per_interval = extra_space // intervals
                extra_space_per_interval_mod = extra_space % intervals

                for _ in range(intervals):
                    word = words.pop(0)
                    line += " "*extra_space_per_interval
                    if extra_space_per_interval_mod > 0:
                        line += " "
                    line += " " + word
                    extra_space_per_interval_mod -= 1

            ret.append(line)

        return ret

if __name__ == "__main__":
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    solution = Solution()

    words = ["What","must","be","acknowledgment","shall","be"]
    # print(solution.fullJustify(words, 20))
    print(solution.fullJustify(words, 16))
