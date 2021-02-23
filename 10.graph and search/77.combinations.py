class Solution(object):
    def combine(self, n, k):
        nums = [i for i in range(1, n + 1)]
        res = []
        def dfs(nums, path, k, index):
            if len(path) == k:
                res.append(path)
                return 
            for i in range(index, n - (k - len(path)) +  2):
                dfs(nums, path + [i], k, i + 1)
        dfs(nums, [], k, 1)
        return res
