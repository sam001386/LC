class Solution(object):
    def permuteUnique(self, A):
        A.sort()
        res = []
        seen = [False for _ in range(len(A))]
        def dfs(path):
            if len(path) == len(A):
                res.append(path[:])
                return 
            for i in range(len(A)):
                if seen[i] == True or (i > 0 and A[i] == A[i - 1] and seen[i - 1] == False):
                    continue 
                seen[i] = True
                dfs(path + [A[i]])
                seen[i] = False
        
        dfs([])
        return res
