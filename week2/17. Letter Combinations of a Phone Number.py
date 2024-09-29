class Solution(object):
    def letterCombinations(self, digits):
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        for i in digits:
            temp = []
            lets = dic[i]
            for j in ans:
                for k in lets:
                    temp.append(j + k)
            if len(ans) == 0:
                for j in lets:
                    temp.append(j)
            ans = temp
        return ans
