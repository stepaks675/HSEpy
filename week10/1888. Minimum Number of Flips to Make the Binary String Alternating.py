def min_flips(s):
    n = len(s)
    s = s + s
    alt1 = "".join(["0" if i % 2 == 0 else "1" for i in range(len(s))])
    alt2 = "".join(["1" if i % 2 == 0 else "0" for i in range(len(s))])

    diff1 = diff2 = 0
    res = float("inf")

    for i in range(len(s)):
        if s[i] != alt1[i]:
            diff1 += 1
        if s[i] != alt2[i]:
            diff2 += 1

        if i >= n:
            if s[i - n] != alt1[i - n]:
                diff1 -= 1
            if s[i - n] != alt2[i - n]:
                diff2 -= 1

        if i >= n - 1:
            res = min(res, diff1, diff2)

    return res
