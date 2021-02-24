class Solution(object):
    def subsetsWithDup(self, A):
        A.sort()
        seen = [False for _ in range(len(A))]
        res = []
        def dfs(index, path):
            res.append(path[:])
            for i in range(index, len(A)):
                if i > 0 and A[i] == A[i - 1] and seen[i - 1] == False:
                    continue
                seen[i] = True
                dfs(i + 1, path + [A[i]])
                seen[i] = False
        
        dfs(0, [])
        return res
