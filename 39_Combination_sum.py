class Solution(object):
    def combinationSum(self, A, target):
        res = []
        self.dfs(A, 0, [], target, res)
        return res

    def dfs(self, A, index, path, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
        for i in range(index, len(A)):
            self.dfs(A, i, path + [A[i]], target - A[i], res)
