class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = [False for _ in range(len(nums))]
        def dfs(index, path):
            if len(path) >= 2:
                res.add(tuple(path[:]))
            for i in range(index, len(nums)):
                if seen[i] == True or (path and nums[i] < path[-1]):
                    continue
                if i > 0 and seen[i - 1] == False and nums[i] == nums[i - 1]:
                    continue
                seen[i] = True 
                dfs(i + 1, path + [nums[i]])
                seen[i] = False 
        dfs(0, [])

        res = list(res)

        return [list(res[i]) for i in range(len(res))]
