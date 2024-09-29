class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        if len(s) == 0:
            return ""

        longest = ""
        for i in range(len(s)):
            substring1 = expand_around_center(i, i)
            substring2 = expand_around_center(i, i + 1)
            if len(substring1) > len(longest):
                longest = substring1
            if len(substring2) > len(longest):
                longest = substring2

        return longest
