# very similar with 207 course schedule question

class Solution:
    def findOrder(self, nums: int, prereq: List[List[int]]) -> List[int]:
        edges = {i: [] for i in range(nums)}
        indegrees = [0 for _ in range(nums)]
        for i, j in prereq:
            edges[j].append(i)
            indegrees[i] += 1
        
        queue = collections.deque()
        count = 0
        result = []
        for i in range(nums):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            result.append(cur)
            count += 1 
            for x in edges[cur]:
                indegrees[x] -= 1
                if indegrees[x] == 0:
                    queue.append(x)
        
        return result if count == nums else []
