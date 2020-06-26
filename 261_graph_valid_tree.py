# BFS approach
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        seen = set()
        graph = collections.defaultdict(list)
        
        # Undirected graph need to add both
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        queue = collections.deque()
        queue.append(0)
        
        while queue:
            node = queue.popleft()
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return len(seen) == n
    
    
# Union-Find approach (w/o optimization)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [-1 for _ in range(n)]
        def find(x):
            while parent[x] != -1:
                x = parent[x]
            return x
        
        for e in edges:
            x = find(e[0])
            y = find(e[1])
            if x == y:
                return False
            parent[x] = y
        
        return len(edges) == n - 1
