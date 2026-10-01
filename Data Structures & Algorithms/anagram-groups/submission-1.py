class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            key = ''.join(sorted(word)) #The reason we use ''.join(sorted(word)) instead of sorted(word) directly is that sorted() returns a list, whereas join() converts that list into a string.
            if key not in group:
                group[key] = []
            group[key].append(word)

        return list(group.values())