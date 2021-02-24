class Solution(object):
    def combinationSum2(self, A, target):
        A.sort()
        seen = [False for _ in range(len(A))]
        res = []
        print(A)
        def dfs(index, path, target):
            if target == 0:
                res.append(path[:])
                return 
            for i in range(index, len(A)):
                if target < 0:
                    continue
                if i > 0 and A[i] == A[i - 1] and seen[i - 1] == False:
                    continue
                seen[i] = True
                dfs(i + 1, path + [A[i]], target - A[i])
                seen[i] = False

        dfs(0, [], target)
        return res 
