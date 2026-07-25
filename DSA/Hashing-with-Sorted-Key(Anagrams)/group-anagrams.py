from collections import defaultdict

def groupAnagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


