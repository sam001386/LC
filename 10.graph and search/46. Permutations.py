class Solution(object):
    def permute(self, A):
        res = [] 
        seen = [False for _ in range(len(A))]
        def dfs(index, path):
            if len(path) == len(A):
                res.append(path[:])
            for i in range(len(A)):
                if seen[i] == False:
                    seen[i] = True
                    dfs(i, path + [A[i]])
                    seen[i] = False
        
        dfs(0, [])
        return res
