class Solution:
    def canFinish(self, num: int, prerequisites: List[List[int]]) -> bool:
        # BFS approach
        # Directed graph
        # Simple topological question
        # 1. start from indegree = 0 points
        # 2. indegree -= 1 everytime
        # 3. if indegree = 0, add it to the queue
        # 4. check whether it is valid topological order
        
        indegree = [0 for _ in range(num)]
        edges = {i : [] for i in range(num)}
        for i, j in prerequisites:
            indegree[i] += 1
            edges[j].append(i)
        
        queue = collections.deque()
        count = 0
        for i in range(num):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            cur = queue.popleft()
            count += 1
            
            for x in edges[cur]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    queue.append(x)
        
        return count == num
