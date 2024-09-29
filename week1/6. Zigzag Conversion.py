class Solution(object):
    def convert(self, s, numRows):
        index = 0
        y = 0
        mas = [""] * numRows
        while index < len(s):
            while y < numRows and index < len(s):
                mas[y] += s[index]
                index += 1
                y += 1
            y -= 2
            while y > 0 and index < len(s):
                mas[y] += s[index]
                index += 1
                y -= 1
        return "".join(mas)
