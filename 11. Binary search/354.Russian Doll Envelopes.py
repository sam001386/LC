class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        if not A:
            return 0
        A.sort(key = lambda x:(x[0], -x[1]))
        arr = [A[0][1]]
        for i in range(len(A)):
            if A[i][1] > arr[-1]:
                arr.append(A[i][1])
            elif A[i][1] < arr[-1]:
                # 1. 这里维护一个单调递增的arr，所以可以用二分法
                # 2. 二分返回在arr中第一个比A[i][1]大的数
                left, right =0, len(arr) - 1
                while left < right:
                    mid = (left + right) // 2 
                    if arr[mid] >= A[i][1]:
                        right = mid
                    else:
                        left = mid + 1 
                arr[left] = A[i][1]
        return len(arr)
