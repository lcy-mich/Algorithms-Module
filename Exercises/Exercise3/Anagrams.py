def anagramGrouper(words):
    sorted_chars = []
    for i, word in enumerate(words):
        sorted_chars.append((sorted(word),i))
    sorted_chars = sorted(sorted_chars)
    currentindex = -1
    grouping = []
    for i, sorted_char in enumerate(sorted_chars):
        if sorted_chars[i - 1][0] != sorted_char[0]:
            grouping.append([])
            currentindex += 1
        grouping[currentindex].append(words[sorted_char[1]])
    return grouping

print(anagramGrouper(["eat", "tea", "part", "ate", "trap", "pass"]))