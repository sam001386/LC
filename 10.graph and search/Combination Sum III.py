class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        seen = [False for i in range(1, 10)]
        res = []
        def dfs(index, path):
            if len(path) == k:
                if sum(path) == n:
                    res.append(path)
                return 
            for i in range(index, len(nums)):
                if len(path) > k:
                    continue 
                if seen[i] == False:
                    seen[i] = True
                    dfs(i + 1, path + [nums[i]]) 
                    seen[i] = False
        dfs(0, [])
        return res
