class Solution(object):
    def combinationSum(self, A, target):
        res = []
        def dfs(path, index, target):
            if target == 0:
                res.append(path)
                return 
            for i in range(index, len(A)):
                if target < 0:
                    continue 
                else:
                    dfs(path + [A[i]], i, target - A[i])
        
        dfs([], 0, target)
        return res
