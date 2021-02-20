class Solution(object):
    def arrayNesting(self, A):
        seen = [False for _ in range(len(A))]
        cur = 0
        index = 0
        res = 0
        while index <= len(A) - 1:
            cur = index
            cur_res = 0
            while not seen[cur]:
                cur_res += 1 
                seen[cur] = True
                cur = A[cur]
            res = max(res, cur_res)
            index += 1
        return res
