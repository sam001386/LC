class Solution(object):
    def combinationSum2(self, A, target):
        res = []
        self.dfs(sorted(A), target, 0, [], res)
        return res

    def dfs(self, A, target, index, path, res):
        if target < 0:
            return
        if target == 0:
            res.append(path[:])
            return 
        for i in range(index, len(A)):
            if i > index and A[i] == A[i - 1]:
                continue
            self.dfs(A, target - A[i], i + 1, path + [A[i]], res)
