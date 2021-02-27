class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n + 1)]
        seen = [False for _ in range(n)]
        res = [0]
        def dfs(path):
            if len(path) == n:
                res[0] += 1 
                return 
            for i in range(n):
                if seen[i]:
                    continue 
                if nums[i] % (len(path) + 1) != 0 and (len(path) + 1) % nums[i] != 0:
                    continue 
                seen[i] = True
                dfs(path + [nums[i]])
                seen[i] = False
        dfs([])
        return res[0]
