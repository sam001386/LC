### Good practice for index sorting: 
### Time complexity: O(n)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        for i in range(len(nums)):
            while 0 <= nums[i] < len(nums) and nums[i] != nums[nums[i]] and nums[i] != i:
                tmp = nums[i]
                nums[i] = nums[tmp]
                nums[tmp] = tmp
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
