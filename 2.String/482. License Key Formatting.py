class Solution(object):
    def licenseKeyFormatting(self, s, k):
        real_string = []
        res = []
        
        for i in range(len(s)):
            if s[i] != "-":
                real_string.append(s[i].upper())

        remain = len(real_string) % k
        cnt = len(real_string) // k
        i = 0
        if remain != 0:
            for i in range(remain):
                res.append(real_string[i])
            if cnt > 0:
                res.append("-")
            i += 1

        while i < len(real_string):
            for _ in range(k):
                res.append(real_string[i])
                i += 1
            if i < len(real_string):
                res.append("-")

        return "".join(res)
