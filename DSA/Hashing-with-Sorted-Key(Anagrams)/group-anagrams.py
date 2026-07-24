from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))