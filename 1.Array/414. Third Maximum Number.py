class Solution(object):
    def thirdMax(self, nums):
        arr = [-2**31-1, -2**31-1, -2**31-1]
        for i in range(len(nums)):
            if nums[i] > arr[0]:
                arr[2] = arr[1]
                arr[1] = arr[0]
                arr[0] = nums[i] 
            elif nums[i] == arr[0]:
                continue
            elif nums[i] > arr[1]:
                arr[2] = arr[1]
                arr[1] = nums[i]
            elif nums[i] == arr[1]:
                continue
            elif nums[i] > arr[2]:
                arr[2] = nums[i]

        if arr[2] == -2**31-1:
            return max(nums)
        else:
            return arr[2]
