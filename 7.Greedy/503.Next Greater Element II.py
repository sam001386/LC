class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        window = len(nums)
        nums = nums + nums
        stack = []
        res = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if i <= window - 1:
                if stack and nums[stack[0]] > nums[i]:
                    res.append(nums[stack[-1]])
                else:
                    res.append(-1)
            stack.append(i)
        return res[::-1]
