# Longest non-repeating sub string.

def longest_non_repeating_sub_string(s):
    start = 0
    maxLength = 0
    lastOccurred = {}

    for i in range( len(s) ):
        if s[i] in lastOccurred and lastOccurred[s[i]] >= start:
            start = lastOccurred[s[i]] + 1

        if i - start + 1 > maxLength:
            maxLength = i - start + 1

        lastOccurred[s[i]] = i

    return maxLength

if __name__ == "__main__":
    print ( longest_non_repeating_sub_string("abbcb") )
