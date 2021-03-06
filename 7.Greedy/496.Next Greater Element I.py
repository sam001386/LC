class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums1))]
        stack = []
        dic = {}
        for i in range(len(nums1)):
            dic[nums1[i]] = i 
        
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[stack[-1]] <= nums2[i]:
                stack.pop()
            if nums2[i] in dic:
                if stack:
                    res[dic[nums2[i]]] = nums2[stack[-1]]
                else:
                    res[dic[nums2[i]]] = -1
            stack.append(i)
        
        return res
