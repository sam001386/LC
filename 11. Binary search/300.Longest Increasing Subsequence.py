# Approach 1: Naive DP
# Time: O(N^2)
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        dp = [1 for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
     
# Approach 2: Binary search
# Time: O(N*log(N))
class Solution:
    def lengthOfLIS(self, A: List[int]) -> int:
        '''
        # Greedy + binary search
        # Maintain an increasing array
        if A[i] < arr[-1]:
            Use binary search to find the first element in "arr" that is larger than A[i]
        ''' 
        if not A:
            return 0
        arr = [A[0]]
        for i in range(1, len(A)):
            if A[i] > arr[-1]:
                arr.append(A[i])
            elif A[i] < arr[-1]:
                # 返回最右
                left, right = 0, len(arr) - 1
                while left < right:
                    mid = (left + right) // 2 
                    if arr[mid] >= A[i]:
                        right = mid 
                    else:
                        left = mid + 1
                arr[left] = A[i]

        return len(arr)
