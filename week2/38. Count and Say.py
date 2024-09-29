class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            stra = self.countAndSay(n - 1)
            ans = ""
            c = 0
            prev = stra[0]
            for i in stra:
                if i == prev:
                    c += 1
                else:
                    ans += str(c)
                    ans += prev
                    c = 1
                prev = i
            if c > 0:
                ans += str(c)
                ans += prev
            return ans
