class Solution(object):
    def findMaxConsecutiveOnes(self, A):
        if not A:
            return 0
        cur = 0 
        res = 0
        if A[0] == 1:
            cur = 1 
            res = 1
        for i in range(1, len(A)):
            if A[i] == 1 and A[i - 1] == 1:
                cur += 1 
            elif A[i] == 1:
                cur = 1 
            else:
                cur = 0
            res = max(res, cur)
            
        return res
