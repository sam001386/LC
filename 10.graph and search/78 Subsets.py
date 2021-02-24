class Solution(object):
    def subsets(self, A):
        res = []
        def dfs(index, path):
            res.append(path[:])
            for i in range(index, len(A)):
                dfs(i + 1, path + [A[i]])

        dfs(0, [])
        return res
