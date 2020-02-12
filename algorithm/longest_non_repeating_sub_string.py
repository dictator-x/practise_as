# Longest non-repeating sub string.

def longest_non_repeating_sub_string(s):
    start = 0
    maxLength = 0
    lastOccurred = {}

    for i, c in enumerate(s):
        if c in lastOccurred and lastOccurred[c] >= start:
            start = lastOccurred[c] + 1

        if i - start + 1 > maxLength:
            maxLength = i - start + 1

        lastOccurred[c] = i

    return maxLength

if __name__ == "__main__":
    print ( longest_non_repeating_sub_string("abbcb") )
