class Solution(object):
    def solveNQueens(self, n):
        if n == 0:
            return []
        res = []
        self.dfs([-1] * n, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                tmp = "." * len(nums)
                self.dfs(nums, index + 1, path + [tmp[: i] + "Q" + tmp[i + 1:]], res)
    
    def valid(self, nums, index):
        for i in range(index):
            if abs(nums[i] - nums[index]) == index - i or nums[i] == nums[index]:
                return False
        return True
