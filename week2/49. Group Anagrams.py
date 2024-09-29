class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        return anagrams.values()
