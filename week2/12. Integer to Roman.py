class Solution(object):
    def intToRoman(self, num):
        output = ""
        # step1
        one = num // 1000
        num %= 1000
        output += one * "M"
        # step2
        two = num // 100
        num %= 100
        if two >= 5:
            if two == 9:
                output += "CM"
            else:
                output += "D"
                output += "C" * (two - 5)
        else:
            if two == 4:
                output += "CD"
            else:
                output += "C" * two
        # step3
        three = num // 10
        num %= 10
        if three >= 5:
            if three == 9:
                output += "XC"
            else:
                output += "L"
                output += "X" * (three - 5)
        else:
            if three == 4:
                output += "XL"
            else:
                output += "X" * three
        # last
        four = num
        if four >= 5:
            if four == 9:
                output += "IX"
            else:
                output += "V"
                output += "I" * (four - 5)
        else:
            if four == 4:
                output += "IV"
            else:
                output += "I" * four
        return output
