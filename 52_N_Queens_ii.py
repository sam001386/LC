class Solution(object):
    def totalNQueens(self, n):
        if n == 0:
            return 0
        self.res = 0
        self.dfs([-1] * n, 0)
        return self.res
    
    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i # record the position of the queue in each row
            if self.valid(nums, index):
                self.dfs(nums, index + 1)
    
    def valid(self, nums, n):
        for cur in range(n):
            if nums[cur] == nums[n] or n - cur == abs(nums[n] - nums[cur]):
                return False
        
        return True
    
