class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        maxl = 0
        seti = set()
        for i in range(0, len(s)):
            l = 0
            seti.clear()
            for j in range(i, len(s)):
                if s[j] in seti:
                    break
                l += 1
                seti.add(s[j])
                maxl = max(l, maxl)
        return maxl
