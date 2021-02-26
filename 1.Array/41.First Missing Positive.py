class Solution(object):
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)
                # 注意因为赋值顺序，
                # 这里不能直接写成：nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[ii]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1 
        
        return len(nums) + 1
    
    def swap(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
